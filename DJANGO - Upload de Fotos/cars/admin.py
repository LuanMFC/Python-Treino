from django.contrib import admin
from cars.models import car, brand

class brandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'color', 'year','mileage', 'plate', 'price', 'photo',)
    search_fields = ('name',)

admin.site.register(brand, brandAdmin)
admin.site.register(car, carAdmin)