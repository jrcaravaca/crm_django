from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from ..models.company_model import Company
from ..forms import ClientCreateForm



@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView): 
    model = Company
    template_name = 'companies/company_list.html'
    context_object_name = 'companies'
    paginate_by = 10

    def get_queryset(self): 
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(cif__icontains=query)  | Q(phone__icontains=query)
            )
        return queryset


# @method_decorator(login_required, name='dispatch')
# class ClientCreateView(CreateView): 
#     template_name = "clients/client_create.html"
#     model = Client
#     success_url = reverse_lazy('clientes')
#     form_class = ClientCreateForm


# @method_decorator(login_required, name='dispatch')
# class ClientDetailView(DetailView): 
#     model = Client
#     template_name = 'clients/client_detail.html'
#     context_object_name = 'client'


# @method_decorator(login_required, name='dispatch')
# class ClientUpdateView(UpdateView): 
#     model= Client
#     template_name = 'clients/client_update.html'
#     form_class = ClientCreateForm
    
#     def get_success_url(self):
#         return reverse('detalle-cliente', kwargs={'pk': self.object.id})


# @method_decorator(login_required, name='dispatch')
# class ClientDeleteView(DeleteView): 
#     model = Client
#     template_name = 'clients/client_delete.html'
#     success_url = reverse_lazy('clientes')
#     context_object_name = 'client'



#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)





    