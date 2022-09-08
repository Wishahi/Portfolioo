from django.db import models
from listings.models import Listing

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=100)
    listing = models.ForeignKey(Listing, related_name='activities', null=True, on_delete=models.CASCADE)
    restaurants = models.TextField(max_length=1000)
    activities = models.TextField(max_length=5000)
    places_to_visit = models.TextField(max_length=5000)
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_7 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_8 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_9 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_10 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_11 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_12 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
