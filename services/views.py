from django.shortcuts import render
from .models import Service, Our_Services
from django.views.generic.base import TemplateView

# Create your views here.
class ServicePageView(TemplateView):
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
      context = super(ServicePageView,self).get_context_data(**kwargs)
      context["services"] = Service.objects.all().order_by('created') [:6]
      context["our_services"]= Our_Services.objects.all()
      return context

