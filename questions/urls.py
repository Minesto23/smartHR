from django.contrib import admin
from django.urls import path
from .views import QuestionsListView

urlpatterns = [
    path('',QuestionsListView.as_view(), name="questions"),
]