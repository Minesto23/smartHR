from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('',PostListView.as_view(), name="blog"),
    path('category/<int:category_id>/',views.category, name="category"),
    path('<int:pk>/<slug:slug>/',PostDetailView.as_view(), name="post"),
]