from django.db import models

# Create your models here.

class brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name
    
class car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    brand = models.ForeignKey(brand, on_delete = models.PROTECT, related_name='car_brand')
    color = models.CharField(max_length=200, null=False)
    year = models.IntegerField(blank=False, null=True)
    mileage = models.IntegerField(blank=False, null=True)
    plate = models.CharField(max_length=10, blank = False, null=True)
    price = models.FloatField(blank=False, null=True)
    photo = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name