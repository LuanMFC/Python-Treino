from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm

# Create your views here.
def list_cars(request):
    cars = Car.objects.all()
    search = request.GET.get("search")
    
    if search:
        cars = Car.objects.filter(model__icontains=search)

    return render(
        request,
        'car_list.html',
        {'cars': cars},
    )

def new_car_forms(request):
    new_car = CarForm()
    return render(
        request,
        'new_car.html',
        {'new_car': new_car}
    )