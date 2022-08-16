from turtle import pos
from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory
from .forms import FilmForm, DirectorForm, PosterForm
from .models import Director, Film
# Create your views here.

context = {'films': Film.objects.all(), 'directors': Director.objects.all()}
def homepage(request):
    # context = {'films': Film.objects.all(), 'directors': Director.objects.all()}
    return render (request, 'homepage.html', context)


def add_film(request):
    context.update({'form': FilmForm})

    PosterFormSet = formset_factory(PosterForm, extra=2)
    if request.method == 'POST':
        form_filled = FilmForm(request.POST)
        formset = PosterFormSet(request.POST)
        if all ([form_filled.is_valid(), formset.is_valid()]):
            form_filled.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    poster = inline_form.save(commit=False)
                    poster.image = form_filled
                    poster.save()
            return redirect('homepage')
        else:
            # print (form_filled.errors) 
            form =FilmForm()
            formset = PosterFormSet


    return render (request, 'add_film.html', context)



def add_director(request):
    context.update({'form': DirectorForm})

    if request.method == 'POST':
        form_filled = DirectorForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print (form_filled.errors)    

    return render (request, 'add_director.html', context)


def update_film(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(instance=film)
    context.update({'form': form})

    if request.method == 'POST':
        filled_form = FilmForm(request.POST, instance=film)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('homepage')
        else:
            return redirect('update_film', args=[id])    

    return render (request, 'update_film.html', context)


def update_director(request, id):
    director = Director.objects.get(id=id)
    form = DirectorForm(instance=director)
    context.update({'form': form})

    if request.method == 'POST':
        filled_form = DirectorForm(request.POST, instance=director)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('homepage')
        else:
            return redirect('update_director', args=[id])    

    return render (request, 'update_director.html', context) 

def director_films(request):
    director = Director.objects.get(id=id)
    films = director.films.all()
    context.update({'director': director,'films': films})

    return render (request, 'director_films.html', context)

