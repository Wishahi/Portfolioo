from django.db import models

# from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    
    name =models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # phone_number = models.PhoneNumberField
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.phone_number
    