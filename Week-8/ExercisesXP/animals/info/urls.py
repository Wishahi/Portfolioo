from django.urls import path
from .views import homepage,show_animal, show_family, posts, add_animal, add_family, update_animal,update_family

urlpatterns = [
    path('homepage', homepage, name='homepage'),
    path('show_animal/<int:id>', show_animal, name='show_animal'),
    path('show_family/<int:id>', show_family, name='show_family'),
    path('posts/<int:familt_id>', posts, name='posts'),
    path('add-animal', add_animal, name='add_animal'),
    path('add-family', add_family, name='add_family'),
    path('update-animal', update_animal, name='update_animal'),
    path('update-family', update_family, name='update_family'),


]
