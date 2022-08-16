# from django.db import models
from tkinter import CASCADE
# from django.db import models
from django.db import models
from django.urls import reverse




# Create your models here.
class FamilyProfile(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name  

    def get_absolute_url(self):
        return reverse('family', args=[self.id])       

class AnimalProfile(models.Model):
    legs = models.IntegerField()
    weight =models.CharField(max_length=50)
    height = models.CharField(max_length=100)
    speed = models.IntegerField()
    family = models.ForeignKey(FamilyProfile, null=True, on_delete=models.CASCADE, related_name='posts')



    def __str__(self) -> str:
        out = f"""
        
        Animal Family:
        """
        for animal in self.family.all():
            out += f"\n{str(animal)}"



    


