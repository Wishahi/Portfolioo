from django import forms
from .models import (
    Customer, 
    Vehicle, 
    VehicleSize, 
    VehicleType, 
    RentalRate, 
    Rental
)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
    
class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'

class RantalForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields = '__all__'

class RantalRateForm(forms.ModelForm):

    class Meta:
        model = RentalRate
        fields = '__all__'

class VehicleSizeForm(forms.ModelForm):

    class Meta:
        model = VehicleSize
        fields = '__all__'

class VehicleTypeForm(forms.ModelForm):

    class Meta:
        model = VehicleType
        fields = '__all__'

