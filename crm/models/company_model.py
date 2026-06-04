from django.db import models

class Company(models.Model): 
    name = models.CharField(max_length=100, verbose_name='Nombre de la Empresa')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    website = models.URLField(verbose_name='Sitio Web')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    cif = models.CharField(max_length=20, unique=True, verbose_name='CIF')
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'