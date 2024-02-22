from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarsInventory


def CreateInventoryCars():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_Value = Sum('price')
    )['total_Value']
    CarsInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    CreateInventoryCars()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    CreateInventoryCars()


    
    