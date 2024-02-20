from cars.models import Car
from cars.forms import CarForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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

class UpdateCars(UpdateView):
    model = Car
    template_name = 'update_cars.html'
    form_class = CarForm
    success_url = "/cars/"

class DeleteCars(DeleteView):
    model = Car
    template_name = 'delete_cars.html'
    success_url = "/cars/"
