from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Stock

# Create your views here.


def index(request):
    stocks = Stock.objects.all()
    return render(request, "portfolio/index.html", {"stocks": stocks})
