from django.contrib import admin
from django.contrib.auth.models import User
from .models.client_model import Client
from .models.company_model import Company
from .models.interaction_model import Interaction

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cif', 'email', 'phone') # Columnas que verás en el listado
    search_fields = ('name', 'cif') # Buscador por nombre o CIF

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'commercial', 'email')
    list_filter = ('company', 'commercial') # Filtros laterales rápidos
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('client', 'contact_channel', 'created_at')
    list_filter = ('contact_channel', 'created_at')