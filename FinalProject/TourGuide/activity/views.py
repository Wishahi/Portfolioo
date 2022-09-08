from unicodedata import name
from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from .models import Activity

# Create your views here.
def listing(request, listing_id):
    listings = get_object_or_404( Listing, pk= listing_id)
    
    queryset_list = listings.activities.all()



    
    print(queryset_list)
    # listing = get_object_or_404(Activity, pk= listing_id)
    context = {
        'listings': listings,
        'list': queryset_list,

    }
   
    return render(request, 'activity/activity.html', context) 
