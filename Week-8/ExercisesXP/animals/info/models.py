# from django.db import models
from tkinter import CASCADE
# from django.db import models
from django.db import models




# Create your models here.
class FamilyProfile(models.Model):
         name=models.CharField(max_length=50)

class AnimalProfile(models.Model):
    legs = models.IntegerField()
    weight =models.CharField(max_length=50)
    height = models.CharField(max_length=100)
    speed = models.IntegerField()
    family = models.ForeignKey(FamilyProfile, null=True, on_delete=models.CASCADE, related_name='posts')



    


