from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .models import UserProfile

from .forms import ProfileForm 

#login_Redirect_url = 'homepage


def signup(request):
    context = {'form': UserCreationForm}
    # logout(request)
    # print(request.user)

    if request.method =='POST':
        form_filled =UserCreationForm(request.POST)
        if form_filled.is_valid():

            form_filled.save(commit = False)

            username = form_filled.cleaned_data.get("username")
            password= form_filled.cleaned_data.get("password1")
           #Authenticate
            user= authenticate(username = username, password = password)

            user = form_filled.save() 
            #create empty profile here once authenticated
            UserProfile.objects.create(user_id= user.id)



            # user = authenticate(username, password)
            # if user is not None:
            regulars = Group.objects.get(name = 'Regulars')
            regulars.user_set.add(user) 
            form_filled.save()
            login(request,user)
                # return redirect('homepage')
            return redirect ('homepage')




        else:
             return render(request, 'signup.html', {'form': form_filled})   

    else:
        return render(request, 'signup.html', context)             



def signin(request):

    if request.user.is_authenticated:
        return redirect ('homepage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password= password)
        if user is not None:
            #login takes reuqest and the user asscoiated
            login(request, user)
            return redirect ('homepage')
        else:
            return render(request, 'signin.html', {'form': AuthenticationForm(request.POST)})    
    else:
        return render (request,'signin.html', {'form': AuthenticationForm} )        




def signout(request):
    # request.user
    if request.user.is_authenticated:
        logout(request)
        return redirect('signin')
    

def update_profile(request):
    profile = request.user.userprofile
    form = ProfileForm(request.POST or None, instance=profile)
    context = {'form': form}

    if form.is_valid():
        form.save()
    return redirect('profile') 

    return render (request, 'update_profile.html', context) 
    
   

def profile(request):
    user = request.User
    profile = user.userprofile
    context= {'profile': profile}

    return render (request, 'profile.html', context)
