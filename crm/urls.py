from django.urls import path

from crm.views.client_views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView
from crm.views.company_views import CompanyListView, CompanyCreateView, CompanyDetailView, CompanyUpdateView, CompanyDeleteView
from crm.views.general_views import HomeView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('clientes/', ClientListView.as_view(), name='clientes'),
    path('clientes/crear/', ClientCreateView.as_view(), name='crear-cliente'),
    path('clientes/detalle/<pk>', ClientDetailView.as_view(), name='detalle-cliente'),
    path('clientes/editar/<pk>', ClientUpdateView.as_view(), name='editar-cliente'),
    path('clientes/eliminar/<pk>', ClientDeleteView.as_view(), name='eliminar-cliente'),

    path('empresas/', CompanyListView.as_view(), name='empresas'),
    path('empresas/crear/', CompanyCreateView.as_view(), name='crear-empresa'),
    path('empresas/detalle/<pk>', CompanyDetailView.as_view(), name='detalle-empresa'),
    path('empresas/editar/<pk>', CompanyUpdateView.as_view(), name='editar-empresa'),
    path('empresas/eliminar/<pk>', CompanyDeleteView.as_view(), name='eliminar-empresa'),
]