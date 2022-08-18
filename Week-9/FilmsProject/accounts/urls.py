
from django.contrib import admin
from django.urls import path
from .views import (
   signup, signin, signout, profile, update_profile, Homepage

)



urlpatterns = [
    path('homepage', Homepage, name='homepage'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='sigin'),
    path('signout', signout, name='signout'),
    # path('create_profile', create_profile, name='create_profile'),
    path('update_profile', update_profile, name='update_profile'),

]