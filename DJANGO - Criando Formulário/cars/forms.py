from django import forms
from cars.models import brand, car

class new_car_form(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(brand.objects.all())
    year = forms.IntegerField()
    color = forms.CharField(max_length=200)
    price = forms.IntegerField()
    image = forms.ImageField()

    def save(self):
        new_car = car(
            model = self.cleaned_data["model"],
            brand = self.cleaned_data["brand"],
            year = self.cleaned_data["year"],
            color = self.cleaned_data["color"],
            price = self.cleaned_data["price"],
            image = self.cleaned_data["image"]
        )
        new_car.save()
        return new_car 