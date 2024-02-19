from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views.generic import ListView, CreateView, DetailView

class List_Cars(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")

        if search:
            cars = super().get_queryset().filter(model__icontains=search)
        
        return cars


class CreateCars(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = "/cars/"

class DetailsCars(DetailView):
    model = Car
    template_name = 'details_cars.html'