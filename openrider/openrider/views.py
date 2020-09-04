from django.shortcuts import render
from accomodation.models import Accomodation, Comment
from django.contrib.auth.models import User


def home(request):
    accomodation_total = Accomodation.objects.count()
    accomodation_comment_total = Comment.objects.count()
    users_total = User.objects.count()
    context = {
        'accomodation_total': accomodation_total,
        'accomodation_comment_total': accomodation_comment_total,
        'users_total': users_total
    }
    return render(request, 'openrider/home.html', context)

def legals(request):
    return render(request, 'openrider/legals.html')