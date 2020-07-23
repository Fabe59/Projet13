from django.urls import path
from . import views

app_name = 'accomodation'
urlpatterns = [
    path('search/', views.search, name="search"),
]