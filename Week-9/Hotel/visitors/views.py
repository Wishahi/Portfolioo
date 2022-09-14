from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# class Homepage(generic.ListView):
#     template_name = 'homepage.html'
#     # context_object_name = "films"
#     success_url ="/homepage"
#

def homepage(request):
    return render(request = request,
                  template_name = "homepage.html")

    
    # def get_queryset(self):
    #     return Lecturer.objects.all()

    # def get_form(self):
    #         form = super(Homepage, self)
    #         # form.fields['release_date'].widget = forms.DateInput(attrs={'type':'date'})
    #         return form    

def signup(request):
    context = {'form': UserCreationForm}
    if request.method == 'POST':
        form_filled = UserCreationForm(request.POST)
        if form_filled.is_valid():
            form_filled.save(commit=False)
            username = form_filled.cleaned_data.get("username")
            password = form_filled.cleaned_data.get("password1")
            #Authenticate
            user = authenticate(username = username, password = password)
            user = form_filled.save()
            login(request,user)
            return redirect('homepage')
        else:
            return render(request, 'signup.html', {'form': form_filled})
    else:
        return render (request, 'signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect ('homepage')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        if user is not None:
            login (request, user)
            return redirect ('homepage')
        else:
            return render (request, 'signin.html', {'form': AuthenticationForm(request.POST)})
    else:
        return render (request, 'signin.html', {'form': AuthenticationForm})

def signout (request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('signin')


