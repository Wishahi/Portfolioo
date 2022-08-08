from django.urls import path
from .views import show_animal, show_family, posts

urlpatterns = [
    
    path('show_animal/<int:id>', show_animal, name='show_animal'),
    path('show_family/<int:id>', show_family, name='show_family'),
    path('posts/<int:familt_id>', posts, name='posts'),


]
