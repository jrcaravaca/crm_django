from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..models.client_model import Client
from ..models.company_model import Company
from ..models.interaction_model import Interaction




@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView): 
    template_name = 'general/home.html'
    
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        
        context['total_clientes'] = Client.objects.count()
        context['total_empresas'] = Company.objects.count()
        context['total_interactions'] = Interaction.objects.count()
        
        return context