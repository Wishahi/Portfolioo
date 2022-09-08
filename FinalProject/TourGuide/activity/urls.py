from django.urls import path
from .views import listing

urlpatterns = [

path('<int:listing_id>/listing', listing, name='listing'),




]