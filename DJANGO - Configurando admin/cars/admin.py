from django.contrib import admin
from cars.models import car

# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'color', 'car_year', 'car_mileage', 'car_price')
    search_fields = ('model',)
    
admin.site.register(car, carAdmin)