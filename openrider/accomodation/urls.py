from django.urls import path
from . import views

app_name = 'accomodation'
urlpatterns = [
    path('add/', views.add, name="add"),
    path('search/', views.search, name="search"),
    path('details/<int:id>', views.details, name="details"),
    path('validation_waiting/', views.validation_waiting, name="validation_waiting"),
    path('validation_checked/', views.validation_checked, name="validation_checked")
]