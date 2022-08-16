
from django.contrib import admin
from django.urls import path
from .views import (
   signup, signin, signout
)



urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', signin, name='sigin'),
    path('signout', signout, name='signout'),

]