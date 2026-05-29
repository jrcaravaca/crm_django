from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from models.client_model import Client


class ClientListView(ListView): 
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    paginate_by = 10