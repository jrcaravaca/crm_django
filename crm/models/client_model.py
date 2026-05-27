from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='clients', verbose_name='Empresa')
    commercial = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clients', verbose_name='Comercial')

    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    position = models.CharField(max_length=200, blank=True, verbose_name='Cargo')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.company.name})"
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'