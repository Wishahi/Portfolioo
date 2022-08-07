from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

person = {
    'Name': 'Leen',
    'Github': 'leen@gmail.com',
    'Address': 'Jerusalem'
}

# profile_user = {
#     'Name': 'Jack',
#     'Gender': 'Male'
# }


def index(request):
    output = " Hello this is my first website"
    # return HttpResponse(output)

    context = {'greeting': output, **person}
    return render(request, 'homepage.html', context )


def profile(request):
    
    names = ['Tom', 'Sasha', 'Yuval']
    gender = ['F', 'M']
    profile = {'name': random.choices(names), 'gender': random.choice(gender)}
    # return render(request, 'profile_user.html', profile_user)
    return render(request, 'profile_user.html', profile)
