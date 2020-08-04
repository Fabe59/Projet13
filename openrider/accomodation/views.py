from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Accomodation
from .forms import AddAccomodationForm
import requests


@login_required
def add(request):
    if request.method == "POST":
        form = AddAccomodationForm(request.POST)
        if form.is_valid():
            new_add = form.save()
    else:
        form = AddAccomodationForm()

    return render(request, 'accomodation/add.html', {'form': form})

def search(request):
    research = request.GET['search']

    if not research:
        return render(request, 'food/home.html')

    result = Accomodation.objects.filter(city__contains=research)
    
    url = "https://nominatim.openstreetmap.org/search/<query>?"
    coordinates_list = []
    for elt in result:
        params = {
            "street": elt.road,
            "city": elt.city,
            "postalcode": elt.zipcode,
            "format": 'json',
        }
        req = requests.get(url, params)
        data = req.json()
        
        element = Accomodation.objects.get(auto_increment_id=elt.auto_increment_id)
        elt.lat = data[0]['lat']
        elt.lon = data[0]['lon']
        
        '''coordinates = data['features'][0]['geometry']['coordinates']
        coordinates_list.append(coordinates)'''


    return render(
        request,
        'accomodation/search.html',
        {
            'research': research,
            'result': result,
        }
        )
