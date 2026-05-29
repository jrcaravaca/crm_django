from django.contrib import admin
from django.urls import path
from views.client_views import ClientListView


urlpatterns = [
    path('client_list/', ClientListView, 'client-list'),
]

