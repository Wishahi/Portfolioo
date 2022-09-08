from django.db import models


# Create your models here.
class Listing(models.Model):
    city = models.CharField(max_length=50)
    description=models.TextField(blank=True)
    population = models.IntegerField()
    direction = models.CharField(max_length=50)
    # temperature = models.IntegerField()
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)



    def __str__(self):
        return self.city