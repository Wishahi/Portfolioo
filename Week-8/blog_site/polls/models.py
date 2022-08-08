from django.db import models

# Create your models here.
class UserProfile(models.model):
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    


