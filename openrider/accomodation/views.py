from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Accomodation
from .forms import AddAccomodationForm
import requests
from math import acos, cos, sin, radians

@login_required
def add(request):
    if request.method == "POST":
        form = AddAccomodationForm(request.POST)
        if form.is_valid():
            new_add = form.save()
    else:
        form = AddAccomodationForm()

    return render(request, 'accomodation/add.html', {'form': form})

@login_required
def search(request):
    research = request.GET['search']

    if not research:
        return render(request, 'food/home.html')

    all_result = Accomodation.objects.all()
    url = "https://nominatim.openstreetmap.org/search/<query>?"
    for elt in all_result:
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
        elt.save()

    result = Accomodation.objects.filter(city__contains=research)
    
    final_result = []
    for elt in all_result:
        dist = 6371 * acos( cos( radians(float(result[0].lat)) ) * cos( radians(float(elt.lat)) ) * cos( radians(float(elt.lon)) - radians(float(result[0].lon)) ) + sin( radians(float(result[0].lat)) ) * sin( radians(float(elt.lat)) ) )
        if dist <= 5:
            final_result.append(elt)
    
    return render(
        request,
        'accomodation/search.html',
        {
            'research': research,
            'final_result': final_result,
            
        }
        )
