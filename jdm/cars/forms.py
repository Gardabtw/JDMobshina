from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'name', 'price', 'description', 'image', 'available',
            'marka_car', 'color_car', 'country_car', 'year_car',
            'mileage_car', 'engine_car', 'transmission_car', 
            'hand_drive', 'type_oil', 'gear_car'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'available': forms.CheckboxInput(),
        }