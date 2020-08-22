from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Accomodation, AddAccomodation ,Comment
from .forms import AddAccomodationForm, CommentForm
import requests
from math import acos, cos, sin, radians
from decimal import *
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def add(request):
    if request.method == "POST":
        form = AddAccomodationForm(request.POST, request.FILES)
        if form.is_valid():
            new_add = form.save()
            return redirect('home')
    else:
        form = AddAccomodationForm()

    return render(request, 'accomodation/add.html', {'form': form})

@login_required
def search(request):
    research = request.GET['search']

    if not research:
        return render(request, 'openrider/home.html')

    all_result = Accomodation.objects.all()
    result = Accomodation.objects.filter(city__contains=research)
    
    if result:
        final_result = []
        for elt in all_result:
            dist = 6371 * acos( cos( radians(Decimal(result[0].lat)) ) * cos( radians(Decimal(elt.lat)) ) * cos( radians(Decimal(elt.lon)) - radians(Decimal(result[0].lon)) ) + sin( radians(Decimal(result[0].lat)) ) * sin( radians(Decimal(elt.lat)) ) )
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
    
    else:
        result = None
        return redirect('home')

@login_required
def details(request, id):
    accomodation = Accomodation.objects.get(auto_increment_id=id)
    comments = Comment.objects.filter(accomodation=accomodation)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(accomodation=accomodation, user=request.user, text=text)
            comment.save()
            return HttpResponseRedirect(accomodation.get_absolute_url())
    else:
        comment_form = CommentForm()

    return render(request, 'accomodation/details.html', {'accomodation': accomodation, 'comments': comments, 'comment_form': comment_form})

@staff_member_required
def validation_waiting(request):
    validation_waiting = AddAccomodation.objects.filter(addAccomodation_statut='Non_lu')

    return render(request, 'accomodation/validation_waiting.html', {'validation_waiting': validation_waiting})

@staff_member_required
def validation_checked(request):
    if request.method == 'POST':
        accomodation = request.POST.get('elt_id')
        accomodation_checked = AddAccomodation.objects.get(addAccomodation_auto_increment_id=accomodation)

        if accomodation_checked.addAccomodation_number is None:
            street = accomodation_checked.addAccomodation_road
        else:
            street = ( str(accomodation_checked.addAccomodation_number) + ' ' + accomodation_checked.addAccomodation_road )

        url = "https://nominatim.openstreetmap.org/search/<query>?"
        params = {
            "street": street,
            "city": accomodation_checked.addAccomodation_city,
            "postalcode": accomodation_checked.addAccomodation_zipcode,
            "format": 'json',
        }
        req = requests.get(url, params)
        data = req.json()
        accomodation_checked.lat = round(Decimal(data[0]['lat']), 6)
        accomodation_checked.lon = round(Decimal(data[0]['lon']), 6)
        accomodation_checked.save()

        print(accomodation_checked.lat)
        print(accomodation_checked.lon)
        verify = Accomodation.objects.filter(lat=accomodation_checked.lat).filter(lon=accomodation_checked.lon)
        print(verify)
        if not verify:
            new_accommodation = Accomodation(
                name = accomodation_checked.addAccomodation_name,
                category = accomodation_checked.addAccomodation_category,
                number = accomodation_checked.addAccomodation_number,
                road = accomodation_checked.addAccomodation_road,
                zipcode = accomodation_checked.addAccomodation_zipcode,
                city = accomodation_checked.addAccomodation_city,
                phone = accomodation_checked.addAccomodation_phone,
                email = accomodation_checked.addAccomodation_email,
                url = accomodation_checked.addAccomodation_url,
                park = accomodation_checked.addAccomodation_parking,
                image = accomodation_checked.addAccomodation_image,
                lat = accomodation_checked.lat,
                lon = accomodation_checked.lon,
                )
            new_accommodation.save()
            accomodation_checked.delete()
        elif verify:
            accomodation_checked.delete()
    
    return redirect('accomodation:validation_waiting')

@staff_member_required
def validation_refused(request):
    if request.method == 'POST':
        accomodation = request.POST.get('elt_id')
        accomodation_checked = AddAccomodation.objects.get(addAccomodation_auto_increment_id=accomodation)
        accomodation_checked.delete()

    return redirect('accomodation:validation_waiting')

