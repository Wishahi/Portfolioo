from django.urls import path
from .views import (get_by_name, get_by_number, get_all)

urlpatterns = [
    path('name/<str:name>', get_by_name, name='get_by_name'),
    path('number/<str:number>', get_by_number, name='get_by_number'),
     path('', get_all, name='get_all'),
  

]
