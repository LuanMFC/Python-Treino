from django.db import models

class car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=200, null=False)
    car_year = models.IntegerField(null=False)
    car_mileage = models.IntegerField(null=False)
    car_price = models.IntegerField(null=False)
