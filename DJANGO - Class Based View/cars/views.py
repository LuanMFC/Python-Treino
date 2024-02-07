from django.shortcuts import render, redirect
from cars.models import car
from cars.forms import new_car_form
from django.views import View

# Create your views here.    

class CarListRender(View):

    def get(self, request):
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
    

class NewCar(View):
    def get(self, request):
        new_car_add = new_car_form()

        return render(
            request, 
            'new_car.html',
            {'new_car_add': new_car_add}
        )
    
    def post(self, request):
        new_car_add = new_car_form(request.POST, request.FILES)
        if new_car_add.is_valid():
            new_car_add.save()
            return redirect("cars_list")
        return render(
        request, 
        'new_car.html',
        {'new_car_add': new_car_add}
    )