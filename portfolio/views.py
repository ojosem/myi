import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import F, ExpressionWrapper, FloatField

from .models import Stock


def index(request):
    # stocks = Stock.objects.all()
    stocks = Stock.objects.annotate(
        investment=ExpressionWrapper(
            F("units") * F("purchase_price"), output_field=FloatField()
        )
    )

    return render(request, "portfolio/index.html", {"stocks": stocks})


def export_csv(request):
    field_names = [field.name for field in Stock._meta.fields][1:] + ["investment"]
    stocks = Stock.objects.annotate(
        investment=ExpressionWrapper(
            F("units") * F("purchase_price"), output_field=FloatField()
        )
    )
    print(field_names)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=portfolio.csv"

    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in stocks:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
