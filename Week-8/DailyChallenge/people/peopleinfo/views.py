from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

    



def people(request):
    newlist = sorted(people, key=lambda k: k['age']) 
    return render(request, 'people.html', newlist)

def people_id(request, id):
 context = people["id"]

 for person in context:
    if id == people["id"]:
     return render(request, 'person.html', person)
 return HttpResponse("Person not found {id}")    
