from django.shortcuts import render
from django.views.generic.list import ListView
from .models import WorkTeam, Who_We_Are

# Create your views here
class WhoListView(ListView):
    model = WorkTeam
    template_name = 'our_team/who.html'

    def get_context_data(self, **kwargs):
        context = super(WhoListView,self).get_context_data(**kwargs)
        context["Who_We_Are"] = Who_We_Are.objects.all() 
        return context
