from django.contrib import admin
from .models import Procurador
from . import form

class ProcuradorAdmin(admin.ModelAdmin):
    form = form.ProcuradorAdminForm
    search_fields = ['nombre']
    
    
    
admin.site.register(Procurador, ProcuradorAdmin)
