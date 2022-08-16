from django.shortcuts import render
from .models import User
from django.http import HttpResponse



def get_by_name(request, name: str) -> HttpResponse:
    user = User.objects.get(name = name)
    return render(request, 'name.html', {'person': user})


def get_by_number(request, number: str) -> HttpResponse:
    user = User.objects.get(phone_number = number)
    return render(request, 'name.html', {'person': user})


def get_all(request):
    users = User.objects.all()
    return render(request, 'person.html', {'persons': users})