from django.contrib import admin
from django.urls import path
from .views import (
   homepage, signup, signin, signout

)



urlpatterns = [
    path('homepage', homepage, name='homepage'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),

]