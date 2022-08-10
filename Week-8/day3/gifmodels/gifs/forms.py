from django import forms
from django.forms import ModelForm
from .models import CategoryModel, GifModel




class GitForm(ModelForm):
      uploader_name = forms.CharField()
      title = forms.CharField()  
      url = forms.URLField()
      categories = forms.ModelMultipleChoiceField(queryset = GifModel.objects.all(), widget = forms.Select())
      class Meta:
        model = GifModel
        fields = ['url'] 

class CategoryForm(ModelForm):
    name = forms.CharField() 
    class Meta:
        model = CategoryModel
        fields = ['name']   
