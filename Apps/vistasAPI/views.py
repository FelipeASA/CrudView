from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.views import APIView

from Apps.empleados.models import EmpleadoModelo, PagoSueldo
from Apps.vistasAPI.serializers import EmpleadoSerializer, PagoSerializer

#def empleadosAPI(request):
#    return HttpResponse('empleadosAPI')

class empleadosAPI(APIView):
    serializer = EmpleadoSerializer

    def get(self, request, format=None):
        datos = EmpleadoModelo.objects.all()
        response = self.serializer(datos, many=True)
        salida = json.dumps(response.data)
        return HttpResponse(salida, content_type='application/json')


def consumoAPI(request):
    return render(request, 'consumoapi.html')


class pagosueldoAPI(APIView):
    serializer = PagoSerializer

    def get(self, request, format=None):
        datos = PagoSueldo.objects.all()
        response = self.serializer(datos, many=True)
        salida = json.dumps(response.data)
        return HttpResponse(salida, content_type='application/json')

