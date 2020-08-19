from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from accomodation.models import Accomodation
from .models import Favorite

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Un compte pour {username} a été créé!')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def save(request):
    if request.method == "POST":
        current_user = request.user
        accomodation = request.POST.get('elt_id')
        accomodation_saved = Accomodation.objects.get(auto_increment_id=accomodation)
        Favorite.objects.get_or_create(
            user=current_user,
            accomodation_saved=accomodation_saved
            )

    return redirect('home')

@login_required
def fav(request):
    current_user = request.user
    favs = Favorite.objects.filter(user=current_user)
    accomodations_favs = [fav.accomodation_saved for fav in favs]

    return render(request, 'users/fav.html', {'accomodations_favs': accomodations_favs})

@login_required
def delete_fav(request):
    if request.method == "POST":
        current_user = request.user
        elt = request.POST.get('fav_id')
        fav = Accomodation.objects.get(auto_increment_id=elt)
        fav_delete = Favorite.objects.filter(user=current_user, accomodation_saved=fav)
        fav_delete.delete()
    return redirect('users:fav') 