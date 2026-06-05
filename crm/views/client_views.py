from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db.models import Q
import csv
from django.http import HttpResponse


from ..models.client_model import Client
from ..forms import ClientCreateForm



@method_decorator(login_required, name='dispatch')
class ClientListView(ListView): 
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self): 
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(company__name__icontains=query) | Q(phone__icontains=query)
            )

        scope = self.request.GET.get('scope')
        if scope:
            if scope == 'mine':
                queryset = queryset.filter(commercial=self.request.user)
            
        return queryset
    
    def get(self, request, *args, **kwargs): 
        if request.GET.get('export') == 'csv':
            return self.export_to_csv()
        return super().get(request, *args, **kwargs)
    
    def export_to_csv(self): 
        clients_to_export = self.get_queryset()
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="clientes.csv"'
        writer = csv.writer(response)
        
        writer.writerow(['Nombre', 'Apellidos', 'Empresa', 'Email', 'Teléfono', 'Comercial Asignado'])

        
        for client in clients_to_export:
            writer.writerow([
                client.first_name,                                              
                client.last_name,                                               
                client.company.name if client.company else 'Sin Empresa',       
                client.email,                                                   
                client.phone,                                                   
                client.commercial.username if client.commercial else 'Sin Asignar' 
            ])

        return response


@method_decorator(login_required, name='dispatch')
class ClientCreateView(CreateView): 
    template_name = "clients/client_create.html"
    model = Client
    success_url = reverse_lazy('clientes')
    form_class = ClientCreateForm

    def form_valid(self, form): 
        form.instance.commercial = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ClientDetailView(DetailView): 
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'


@method_decorator(login_required, name='dispatch')
class ClientUpdateView(UpdateView): 
    model= Client
    template_name = 'clients/client_update.html'
    form_class = ClientCreateForm
    
    def get_success_url(self):
        return reverse('detalle-cliente', kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class ClientDeleteView(DeleteView): 
    model = Client
    template_name = 'clients/client_delete.html'
    success_url = reverse_lazy('clientes')
    context_object_name = 'client'



    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)





    