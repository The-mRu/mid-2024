from django.urls import path
from django.shortcuts import render
from django.contrib import admin
from . import views
from .views import CustomerContactView
urlpatterns = [
    path('', views.home, name='home'),
    path('update-contact/', CustomerContactView.as_view(), name='update-contact'),
]

