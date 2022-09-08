from django.shortcuts import render, get_object_or_404
from .models import Listing
from listings.choices import direction_choices, city_choices
from django.core.paginator import Paginator
from django.db.models import Q
import requests



# Create your views here.

def index(request):
   
    keywords = request.GET.get('keywords')
    keywords= keywords if keywords != '' else "〠"

    city = request.GET.get('city')
    city = city_choices.get(city,"〠" )
    direction = request.GET.get('direction')
    direction = direction_choices.get(direction, "〠")
    # print(request.GET)
    # print(keywords)
    # print(city)
    # print(direction)

    
    listings = Listing.objects.filter(Q(city__iexact = city ) ^ Q(description__icontains =keywords  ) ^ Q(direction__iexact = direction))

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6d6fb8c0b9cf483b0d3ece345d8ea4b1'
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
    
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    mylist = zip(paged_listings, weather_data)
    context = {
        # 'listings': paged_listings,
        # 'weather':weather_data
        'mylist' : mylist
    }
   


    return render(request, 'listings/listings.html', context)






def search(request):
  queryset_list = Listing.objects.all()

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # Direction
  if 'direction' in request.GET:
    direction = request.GET['direction']
    if direction:
      queryset_list = queryset_list.filter(direction__iexact=direction)

  


  context = {
    'city_choices': city_choices,
    'direction_choices': direction_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)

