from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from ..models import Interaction, Client
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class InteractionCreateView(CreateView): 
    model = Interaction
    fields = ['contact_channel', 'content']
    template_name = 'interactions/interaction_create.html'

    def form_valid(self, form): 
        client_id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=client_id)
        form.instance.client = client
        return super().form_valid(form)
    
    def get_success_url(self): 
        return reverse_lazy('detalle-cliente', kwargs={'pk': self.object.client.id})