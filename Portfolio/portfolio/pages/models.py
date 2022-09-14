from django.db import models

# Create your models here.
class Information(models.Model):
    uni_name= models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    grade = models.CharField(max_length=200, blank=True)
    place = models.CharField(max_length=200)
    year = models.CharField(max_length=200)


    def __str__(self):
        return self.uni_name