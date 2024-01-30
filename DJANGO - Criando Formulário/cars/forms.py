from django import forms
from cars.models import car

class new_car_form(forms.ModelForm):
    
    class Meta:
        model = car
        fields = ("__all__")
