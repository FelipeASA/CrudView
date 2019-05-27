from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.core import serializers

from Apps.empleados.models import EmpleadoModelo
from Apps.empleados.forms import EmpleadoForm

class listar(ListView):
    model = EmpleadoModelo
    template_name = 'listar.html'

class crear(CreateView):
    model = EmpleadoModelo
    form_class = EmpleadoForm
    template_name = 'crear.html'
    success_url = reverse_lazy('listar')    

class editar(UpdateView):
    model = EmpleadoModelo
    form_class = EmpleadoForm
    template_name = 'editar.html'
    success_url = reverse_lazy('listar')   

class eliminar(DeleteView):
    model = EmpleadoModelo
    template_name = 'eliminar.html'
    success_url = reverse_lazy('listar')   

def home(request):
    return render(request, 'home.html')

