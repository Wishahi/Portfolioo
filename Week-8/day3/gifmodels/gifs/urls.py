from django.urls import path
from .views import all_gifs, uploadgif, uploadcategory, category_form, all_categories, all_gifimages


urlpatterns = [

    path('all/', all_gifs, name='all'),
    path('category_form/', category_form, name = 'category_form'),
    path('uploadcategory/', uploadcategory, name = 'uploadcategory'),
    path('uploadgif/', uploadgif, name = 'uploadgif'),
    path('all_categories/', all_categories, name = 'all_categories'),
    path('all_gifimages/<int:id>', all_gifimages, name='all_gifimages'),

]


