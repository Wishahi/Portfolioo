from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import GifModel, CategoryModel
from .forms import CategoryForm, GitForm
# Create your views here.



# def home(request):
#     return HttpResponse("ok")


def all_gifs(request):
    context = {'title': 'Gifs', 'gifs': GifModel.objects.all()}
    return render(request, 'gifs.html', context)


def uploadgif(request):
    if request.POST:
        form = GitForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            form.save()
        return HttpResponse("great gif")
    return render(request, 'addgif.html', {'form': GitForm})    


def uploadcategory(request):
    if request.POST:
        form = CategoryForm(request.POST, request.FILES)
        print (request.FILES)
        if form.is_valid:
            form.save()
        return HttpResponse("great")
    return render(request, 'addcategory.html', {'form': CategoryForm})        




def category_form(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # form_name = form['name'].value
            form_name = form.cleaned_data['name']
            # context['formInfo'] = [form_name]
            category = CategoryModel.objects.get(name = form_name)
            gifs = category.gifs.all()
            context = {'title': 'GifsCategory', 'gifs': gifs}

        return render(request, 'categoryform.html', context)

    form = CategoryForm()
    context = {'title': 'GifsCategory', 'form': form}
    return render(request, 'categoryform.html', context)


def all_categories(request):
    context = {'title': 'Category', 'categories': CategoryModel.objects.all()}
    return render(request, 'category.html', context)



def all_gifimages(request, id: int) -> HttpResponse:

    gif_selected = None

    for gif in GifModel:
        if gif['id'] == id:
            gif_selected: dict = gif

    return render(request, 'gifimage.html', gif_selected)    