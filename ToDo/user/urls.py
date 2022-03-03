from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('', views.home),
    path('1', views.usercreate)
]