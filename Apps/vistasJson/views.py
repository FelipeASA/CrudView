from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core import serializers

from Apps.empleados.models import EmpleadoModelo

#  vista con salida en formato json
def empleadojson(request):
    datos = EmpleadoModelo.objects.all()
    response_json = serializers.serialize('json', datos)
    return HttpResponse(response_json, content_type='application/json')

def consumojson(request):
    return render(request, 'consumojson.html')

