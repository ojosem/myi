from django.db import models

# Create your models here.


class Stock(models.Model):
    code = models.CharField(max_length=10)
    units = models.IntegerField()
    purchase_price = models.FloatField()
    purchase_date = models.DateField()
