from django.shortcuts import render
from .models import Question
from django.views.generic.list import ListView

class QuestionsListView(ListView):
    model = Question
    template_name = 'questions/questions.html'