from django.db import models

# Create your models here.
class brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name

class car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=200)
    car_brand = models.ForeignKey(brand, on_delete=models.PROTECT, related_name="cars_brands")
    car_color = models.CharField(max_length=200)
    car_price = models.FloatField()
    car_year = models.IntegerField()
    car_mileage = models.IntegerField()

    def __srt__(self):
        return self.car_name