from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ("__all__")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 3000.0:
            self.add_error('price', "Insira um valor MAIOR que R$2000  ")
        return price