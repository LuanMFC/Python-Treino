from django.shortcuts import render
from cars.models import car
from cars.forms import new_car_form
# Create your views here.
def renderizar(request):

    cars = car.objects.all()

    search = request.GET.get("search")
    if search:
        cars = car.objects.filter(model__icontains=search)

    print(cars)
    return render(
        request, 
        'cars.html',
        {'cars': cars} 
    )


def new_car(request):
    new_car_add = new_car_form()

    return render(
        request, 
        'new_car.html',
        {'new_car_add': new_car_add}
    )