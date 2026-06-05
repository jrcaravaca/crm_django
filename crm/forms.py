from .models import Client, Company

from django import forms

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company', 'first_name', 'last_name', 'email', 'phone', 'position']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)