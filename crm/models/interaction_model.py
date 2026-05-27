from django.db import models
from ..constants import CANALES



class Interaction(models.Model): 
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='interactions', verbose_name='Cliente')
    contact_channel = models.CharField(choices=CANALES, verbose_name='Canal de Contacto')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    content = models.TextField(verbose_name='Contenido')
    
    def __str__(self):
        return f"{self.contact_channel} con {self.client.first_name} - {self.created_at.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = 'Interacción'
        verbose_name_plural = 'Interacciones'

