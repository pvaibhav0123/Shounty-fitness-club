from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views



urlpatterns = [
    path("", views.index, name='index'),
    path("registration/", views.registration, name='registration'),
    path("trainers/", views.trainers, name='trainers'),
    path("membership/", views.membership, name='membership'),
    path("contact/", views.contact, name='contact'),
    path("gallery/", views.gallery, name='gallery')
]
