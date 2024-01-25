from django.shortcuts import render
from cars.models import car
# Create your views here.
def renderizar(request):
    cars = car.objects.all()
    return render(
        request, 
        'cars.html',
        {'cars': cars} 
    )