from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import F, ExpressionWrapper, FloatField

from .models import Stock

# Create your views here.


def index(request):
    # stocks = Stock.objects.all()
    stocks = Stock.objects.annotate(
        investment=ExpressionWrapper(
            F("units") * F("purchase_price"), output_field=FloatField()
        )
    )

    return render(request, "portfolio/index.html", {"stocks": stocks})
