from multiprocessing import context
from django.shortcuts import render
import json 
from django.http import HttpResponse
from .models import FamilyProfile, AnimalProfile
# Create your views here.
import sys


sys.path.append('./info')
f = open('info/animal_family.json')
data = json.load(f)
f.close()

def show_animal(request, id):
    context = data["animals"]

    for animal in context:
        if id == animal["id"]:
         return render(request, 'animal.html', animal)
    return HttpResponse("Animal not found {id}")


def show_family(request, id):
    context = data["families"]

    for family in context:
        if id == family["id"]:
         return render(request, 'family.html', family)
    return HttpResponse("family not found {id}")


def posts(request, family_id: int) -> HttpResponse:
    animal = AnimalProfile.get(family_id)
    posts = animal.posts
    return render(request, 'posts.html', {'posts': posts})
     