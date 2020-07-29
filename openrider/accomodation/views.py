from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddAccomodationForm


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

    return render(
        request,
        'accomodation/search.html',
        {
            'research': research,
            'result': result,
        }
        )
