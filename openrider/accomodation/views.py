from django.shortcuts import render
from .models import Accomodation


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
