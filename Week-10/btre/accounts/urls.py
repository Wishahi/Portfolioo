from django.urls import path
from .views import signin, signup, signout

urlpatterns = [
path('login',signin, name='login'),
path('register', signup, name='register'),
path('logout', signout, name='logout'),



]