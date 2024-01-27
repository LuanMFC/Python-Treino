from django import forms
from cars.models import brand

class new_car_form(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(queryset=brand.objects.all())
    year = forms.IntegerField()
    color = forms.CharField(max_length=200)
    price = forms.IntegerField()
    image = forms.ImageField()