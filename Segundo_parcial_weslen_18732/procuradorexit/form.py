from django import forms
from django.contrib import admin
from .models import Procurador

class ProcuradorAdminForm(forms.ModelForm):
    class Meta:
        model = Procurador
        fields = '__all__'

