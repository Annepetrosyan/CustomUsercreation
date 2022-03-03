from django.contrib import admin
from django.urls import path
from Task import views

urlpatterns = [
    path('', views.home),
]