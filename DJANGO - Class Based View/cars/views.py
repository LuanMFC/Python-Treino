from django.shortcuts import render, redirect
from cars.models import car
from cars.forms import new_car_form
from django.views.generic import ListView, CreateView, DetailView

# Create your views here.    
class CarListRender(ListView):
    model = car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCar(CreateView):
    model = car
    form_class = new_car_form
    template_name = 'new_car.html'
    success_url = 'cars'

class DetailsViewCars(DetailView):
    model = car
    template_name = "details.html"