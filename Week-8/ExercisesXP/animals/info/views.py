from multiprocessing import context
from django.shortcuts import render, redirect
import json 
from django.http import HttpResponse
from .models import FamilyProfile, AnimalProfile
from .forms import FamilyForm, AnimalForm
# Create your views here.
import sys


sys.path.append('./info')
f = open('info/animal_family.json')
data = json.load(f)
f.close()

def homepage(request):
    
    return render (request, 'homepage.html', {})

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
     


def add_animal(request):
    context = ({'form': AnimalForm})

    if request.method == 'POST':
        form_filled = AnimalForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print (form_filled.errors)    

    return render (request, 'add_animal.html', context)

def add_family(request):
    context =({'form': FamilyForm})

    if request.method == 'POST':
        form_filled = FamilyForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print (form_filled.errors)    

    return render (request, 'add_family.html', context)


def update_animal(request, id):
    animal = AnimalProfile.objects.get(id=id)
    form = AnimalProfile(instance=animal)
    context =({'form': form})

    if request.method == 'POST':
        filled_form = AnimalForm(request.POST, instance=animal)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('homepage')
        else:
            return redirect('update_animal', args=[id])    

    return render (request, 'update_animal.html', context)


def update_family(request, id):
    family = FamilyProfile.objects.get(id=id)
    form = FamilyForm(instance=family)
    context=({'form': form})

    if request.method == 'POST':
        filled_form = FamilyForm(request.POST, instance=family)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('homepage')
        else:
            return redirect('update_family', args=[id])    

    return render (request, 'update_family.html', context) 