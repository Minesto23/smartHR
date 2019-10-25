from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from blog.models import Post   # Import models from Blog, Questions and  Services for the dinamic Home
from questions.models import Question
from services.models import Service
from .forms import ContactForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

class DinamicHome(TemplateView):
    template_name = 'core/home.html'
        
    def get_context_data(self, **kwargs):
      context = super(DinamicHome,self).get_context_data(**kwargs)
      context["questions"]= Question.objects.all().order_by('-created')[:2]
      context["services"] = Service.objects.all().order_by('created')[:6]
      context["posts"]= Post.objects.all().order_by('-created')[:3]
      return context


