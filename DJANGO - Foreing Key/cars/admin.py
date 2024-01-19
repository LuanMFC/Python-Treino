from django.contrib import admin
from cars.models import car, brand

# Register your models here.

class brandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)

class carAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_brand', 'car_color', 'car_price', 'car_year', 'car_mileage',)
    search_fields = ('car_name',)

admin.site.register(car, carAdmin)
admin.site.register(brand, brandAdmin)