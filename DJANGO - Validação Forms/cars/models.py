from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, null=False)
    brand = models.ForeignKey(Brand, on_delete = models.PROTECT, related_name = 'car_brand')
    color = models.CharField(max_length=200, null=False)
    factory_year = models.IntegerField(blank=True, null=True)
    car_year = models.IntegerField(null = False)
    mileage = models.IntegerField(null = False)
    plate = models.CharField(max_length=10, blank=True, null = True)
    price = models.FloatField(blank=False, null=False)
    image = models.ImageField(upload_to='car')

    def __str__(self):
        return self.model

class CarsInventory(models.Model):
    cars_count = models.IntegerField(null =False)
    cars_value = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def Meta(self):
        ordering = ('-cars_count')

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
       