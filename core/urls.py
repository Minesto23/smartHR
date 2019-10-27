from django.contrib import admin
from django.urls import path
from . import views
from .views import DinamicHome

urlpatterns = [
    path('',DinamicHome.as_view(), name="home"),
]