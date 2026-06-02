from django.urls import path

from crm.views.client_views import ClientListView, ClientCreateView
from crm.views.general_views import HomeView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clientes/', ClientListView.as_view(), name='clientes'),
    path('clientes/crear/', ClientCreateView.as_view(), name='crear_clientes'),
    
]