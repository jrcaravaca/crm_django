from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, FormView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy



@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView): 
    template_name = 'general/home.html'
    context_object_name = 'clients'
    