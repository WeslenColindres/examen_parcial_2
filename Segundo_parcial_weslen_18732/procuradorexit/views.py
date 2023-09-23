from django.shortcuts import render
from .models import Procurador
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect

class ProcuradorListView(ListView):
    model = Procurador
    permission_required = 'procuradorexit.view_procurador'
    template_name = 'list.html'
    context_object_name = 'procuradores'
    def get_queryset(self):
        query = self.request.GET.get('procurador')
        if query:
            return Procurador.objects.filter(Q(nombre__icontains=query)) 
        else:
            return Procurador.objects.all()

class ProcuradorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'procuradorexit.view_procurador'
    model = Procurador
    template_name = 'detalles.html'
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('procurador_list'))

class ProcuradorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'procuradorexit.add_procurador'
    model = Procurador
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('procurador_list')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('procurador_list'))

class ProcuradorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'procuradorexit.change_procurador'
    model = Procurador
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('procurador_list')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('procurador_list'))

class ProcuradorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'procuradorexit.delete_procurador'
    model = Procurador
    template_name = 'eliminar.html'
    success_url = reverse_lazy('procurador_list')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('procurador_list'))
    
def home_view(request):
    return render(request, 'base.html')