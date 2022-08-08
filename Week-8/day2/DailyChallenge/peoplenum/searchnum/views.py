from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse


def phoneNumber(request, phoneNumber):
    

    for personnumber in UserProfile:
        if phoneNumber == personnumber["phoneNumber"]:
         return render(request, 'person.html', personnumber)
    return HttpResponse("Number not found {phoneNumber}")

def name(request, name):
    

    for nameperson in UserProfile:
        if name == nameperson["name"]:
         return render(request, 'name.html', nameperson)
    return HttpResponse("Person not found {name}")    
