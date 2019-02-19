from django.contrib import admin

# Register your models here.
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "units", "purchase_date", "purchase_price")


admin.site.register(Stock, StockAdmin)
