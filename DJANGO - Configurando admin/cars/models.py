from django.db import models

# Create your models here.
class car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=200, null=False)
    car_year = models.IntegerField(null=False)
    car_mileage = models.IntegerField(null=False)
    car_price = models.FloatField()

    
    def __str__(self):
        return self.model