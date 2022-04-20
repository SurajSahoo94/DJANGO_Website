from django.contrib import admin
from django.urls import path
from home_app import views

urlpatterns = [
    path("", views.home, name = 'home_app'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
    path("contact", views.contact, name = 'contact'),
]
