from django.db import models

# Create your models here.


class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    units = models.IntegerField()
    purchase_price = models.FloatField()
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.code}: {self.name}"
