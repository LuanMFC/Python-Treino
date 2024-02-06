from django.contrib import admin
from cars.models import brand, car

# Register your models here.
class brandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =('name',)

class carsAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'year', 'color', 'price',)
    search_fields = ('model',)

admin.site.register(brand, brandAdmin)
admin.site.register(car, carsAdmin)