from django.contrib import admin
from django.urls import path
from .views import WhoListView

urlpatterns = [
    path('',WhoListView.as_view(), name="who"),
]