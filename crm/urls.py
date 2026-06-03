from django.urls import path

from crm.views.client_views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView
from crm.views.general_views import HomeView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clientes/', ClientListView.as_view(), name='clientes'),
    path('clientes/crear/', ClientCreateView.as_view(), name='crear-cliente'),
    path('clientes/detalle/<pk>', ClientDetailView.as_view(), name='detalle-cliente'),
    path('clientes/editar/<pk>', ClientUpdateView.as_view(), name='editar-cliente'),
]