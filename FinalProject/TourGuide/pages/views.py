
from unittest import result
from django.shortcuts import render
from listings.models import Listing
from listings.choices import direction_choices, city_choices
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests

# Create your views here.

from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
def home(request):
      listings = Listing.objects.all()
      context = {
        'listings': listings,
        'city_choices': city_choices,
        'direction_choices': direction_choices,
      
        
    }
    
      return render (request, 'base.html',context)

def about(request):
   
    return render (request, 'about.html')



def all(request):
  listings = Listing.objects.all()

  city = request.GET.get('city')
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6d6fb8c0b9cf483b0d3ece345d8ea4b1'
  city_weather = requests.get(url.format(city)).json()
  weather_data = []
    

  for city in listings:
      

      city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

      weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

      weather_data.append(weather)
    # print(weather_data)  
    #  
  page = request.GET.get('page',1)
  paginator = Paginator(listings,20)
  
  try:
     results = paginator.page(page)
  except PageNotAnInteger:
    results = paginator.page(1)
  except EmptyPage:
    results = paginator.page(paginator.num_pages)   
  # print(paginator.num_pages)    

  mylist = zip(results, weather_data)
  context = {
        # 'listings': paged_listings,
        # 'weather':weather_data
        
        'mylist' : mylist
    }
    
  # page1= paginator.page(1)
  # print(page1.object_list)


  return render (request, 'listings/listings.html', context)