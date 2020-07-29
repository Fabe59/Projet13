from django.urls import path
from . import views

app_name = 'accomodation'
urlpatterns = [
    path('add/', views.add, name="add"),
    path('search/', views.search, name="search"),
]