from django.urls import path
from .views import  home,about,all



urlpatterns = [

path('', home, name='home'),
path('about', about, name='about'),
path('all', all, name='all'),
] 
