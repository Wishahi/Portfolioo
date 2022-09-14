from django.shortcuts import render
from .models import Information

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


# def about(request):
#     info = Information.objects.all()

#     context = {
#         info : 'info'
#     }  
    
#     return render (request, 'skills.html', context)
    # return render(request, 'test.html')

def skills(request):
   
    
    return render(request, 'skills.html')