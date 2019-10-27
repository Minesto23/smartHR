from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.contact, name="contact"),
    path('ajax/load_turns/',views.Load_Turns, name="ajax-loadturns")
]