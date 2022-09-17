from django.shortcuts import render, redirect

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

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
   
    
    return render(request, 'index.html')


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["leenwishahi@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("index.html")
    return render(request, "index.html", {"form": form})

