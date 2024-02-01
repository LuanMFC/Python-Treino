from django.contrib import admin
from cars.models import Brand, Car

class adminBrand(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class adminCar(admin.ModelAdmin):
    list_display = ('model', 'brand', 'color', 'factory_year', 'car_year','mileage', 'plate', 'price',)
    search_fields = ('model',)

admin.site.register(Brand, adminBrand)
admin.site.register(Car, adminCar)

# Register your models here.
