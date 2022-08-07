from django.urls import path
from .views import people, people_id

urlpatterns = [
    
    path('people', people, name='people'),
    path('people_id/<int:id>', people_id, name='people_id'),


]
