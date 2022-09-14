from django.db import models
from django.urls import reverse
from faker import Faker
from datetime import date
import random 

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class VehicleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class VehicleSize (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.FloatField()
    size= models.ForeignKey(VehicleSize,max_length=50, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        out = f"""Vehicle: {self.vehicle_type.name} | {self.size.name} |"""
        return out

    def get_absolute_url(self):
        return reverse('vehicle', args = [self.id])

class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicle_type', on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, related_name='vehicle_size', on_delete=models.CASCADE)

class Rental(models.Model):
    rental_date = models.DateField(blank=True)
    return_date = models.DateField(blank=True)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE, blank=True)
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle', on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):

        fake = Faker()

        rental_date = fake.date_between(start_date = date(2022, 1, 1))
        rand_int = random.randint(0,10)

        if rand_int > 5:
            return_date = None
        else:
            return_date = fake.date_between(start_date = rental_date)
        rand_cust_idx = random.randint(1, 101)

        customer = Customer.object.get(id=rand_cust_idx)

        amount_vehicles = len(Vehicle.objects.all())
        rand_vehicle_idx = random.randint(1, amount_vehicles + 1)

        vehicle = Vehicle.objects.get(id = rand_vehicle_idx)

        kwargs = {
        'rental_date' : rental_date,
         'return_date': return_date,
         'customer': customer,
         'vehicle': vehicle}

        self.super(Rental, self).save(*args, **kwargs)
