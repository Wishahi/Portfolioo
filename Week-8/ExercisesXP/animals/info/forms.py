from django import forms
from datetime import date
from.models import (
FamilyProfile, AnimalProfile
)


class FamilyForm(forms.ModelForm):
    class Meta:
        model = FamilyProfile
        fields = '__all__'
        

class AnimalForm(forms.ModelForm):
    class Meta:
        model = AnimalProfile
        fields = '__all__'
        widgets = {
            'family': forms.TextInput
            

        }

