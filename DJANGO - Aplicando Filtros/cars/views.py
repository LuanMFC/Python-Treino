from django.shortcuts import render
from cars.models import car
# Create your views here.
def renderizar(request):

    cars = car.objects.all()

    search = request.GET.get("search")
    if search:
        cars = car.objects.filter(name__icontains=search)

    print(cars)
    return render(
        request, 
        'cars.html',
        {'cars': cars} 
    )