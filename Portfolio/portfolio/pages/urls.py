from django.urls import path
from .views import index,skills



urlpatterns = [

path('', index, name='index'),
path('skills/', skills, name='skills'),


]