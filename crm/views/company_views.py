from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db.models import Q
import csv
from django.http import HttpResponse

from ..models.company_model import Company
from ..forms import CompanyCreateForm



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
    
    def get(self, request, *args, **kwargs): 
        if request.GET.get('export') == 'csv':
            return self.export_companies_to_csv()
        return super().get(request, *args, **kwargs)
    
    def export_companies_to_csv(self):
            companies_to_export = self.get_queryset()

            response = HttpResponse(content_type='text/csv; charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename="empresas_crm.csv"'
            response.write('\ufeff') 
            
            writer = csv.writer(response)
            
            
            writer.writerow([
                'Nombre Empresa', 
                'Sitio Web', 
                'Teléfono', 
                'Email Corporativo',
                'Contacto Principal',       
                'Email del Contacto'        
            ])

            for company in companies_to_export:
                
                main_contact = company.clients.first() 
                
               
                if main_contact:
                    contact_name = f"{main_contact.first_name} {main_contact.last_name}"
                    contact_email = main_contact.email
                else:
                    contact_name = "Sin contactos"
                    contact_email = "-"

                
                writer.writerow([
                    company.name,
                    company.website if hasattr(company, 'website') else 'No tiene',
                    company.phone if hasattr(company, 'phone') else 'No tiene',
                    company.email if hasattr(company, 'email') else 'No tiene',
                    contact_name,   
                    contact_email   
                ])

            return response


@method_decorator(login_required, name='dispatch')
class CompanyCreateView(CreateView): 
    template_name = "companies/company_create.html"
    model = Company
    success_url = reverse_lazy('empresas')
    form_class = CompanyCreateForm


@method_decorator(login_required, name='dispatch')
class CompanyDetailView(DetailView): 
    model = Company
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'


@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(UpdateView): 
    model= Company
    template_name = 'companies/company_update.html'
    form_class = CompanyCreateForm
    
    def get_success_url(self):
        return reverse('detalle-empresa', kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class CompanyDeleteView(DeleteView): 
    model = Company
    template_name = 'clients/client_delete.html'
    success_url = reverse_lazy('clientes')
    context_object_name = 'company'



    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)





    