from django import forms
from datetime import date
from.models import (
Director,
Film
)


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'released_date': forms.DateInput(attrs= {'type': 'date'}) 
            # 'released'_date : forms.Date

        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
