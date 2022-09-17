from django.urls import path
from .views import index,skills, contactView



urlpatterns = [

path('', index, name='index'),
path('skills/', skills, name='skills'),
path('contactView/', contactView, name='contactView'),



]