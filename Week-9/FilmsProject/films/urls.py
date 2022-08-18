
from django.contrib import admin
from django.urls import path
from .views import (
    delete_director,
    Homepage,
    homepage,
    add_film,
    add_director,
    DeleteFilm,
    AddComment,
    DeleteDirector,
    update_film,
    update_director,
    director_films,
    rate
)



urlpatterns = [
    path('homepage', homepage, name='homepage'),
    path('add-film', add_film, name='add_film'),
    path('add-director', add_director, name='add_director'),
    path('update-film/<int:id>', update_film, name='update_film' ),
    path('update-director/<int:id>', update_director, name='update_director' ),
    path('director-films/<int:id>', director_films, name='director_films' ),
    path ('homepage',Homepage.as_view, name='homepage'),
    path ('delete-film',DeleteFilm.as_view, name='delete_film'),
    path ('add-comment',AddComment.as_view, name='add_comment'),
    path ('delete-director',DeleteDirector.as_view, name='delete_director'),
    path('add-rate', rate, name='rate'),
]
