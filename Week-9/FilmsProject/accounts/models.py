from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    hobbies = models.CharField(max_length=100)
    image = models.URLField()
    address= models.CharField(max_length=100)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
# Create your models here.

    def __str__(self) -> str:
        return self.user.usernane

        
