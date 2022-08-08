from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
# Create your models here.
class UserProfile(models.model):
    
    name =models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.PhoneNumberField
    address = models.CharField(max_length=100)

