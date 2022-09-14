from django.shortcuts import render
from .forms import (
    VehicleForm,
    VehicleSize,
    VehicleSizeForm,
    VehicleType,
    VehicleTypeForm
    )
from .models import (
    Vehicle
)
# Create your views here.
def add_vehicle(request):

    context = {'form': VehicleForm}
    if request.method == 'POST':

        vehicle_form = VehicleForm(request.POST)

        if vehicle_form.is_valid():
            filled_form = vehicle_form.save()

    return render(request, 'add_vehicle.html', context)

def add_vehicleType(request):

    context = {'form': VehicleTypeForm}
    if request.method == 'POST':

        vehicle_form = VehicleTypeForm(request.POST)

        if vehicle_form.is_valid():
            filled_form = vehicle_form.save()

    return render(request, 'add_vehicle.html', context)

def add_vehicleSize(request):

    context = {'form': VehicleSizeForm}
    if request.method == 'POST':

        vehicle_form = VehicleSizeForm(request.POST)

        if vehicle_form.is_valid():
            filled_form = vehicle_form.save()

    return render(request, 'add_vehicle.html', context)

def show_vehicle(request, id):
    vehicle_chosen = Vehicle.objects.get(id=id)
    return render(request, 'show_vehicle.html', {'vehicle': vehicle_chosen})

def show_vehicles(request):

    vehicle_all = Vehicle.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicle_all})
