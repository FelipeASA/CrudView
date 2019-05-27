from rest_framework.serializers import ModelSerializer

from Apps.empleados.models import EmpleadoModelo, PagoSueldo

class EmpleadoSerializer(ModelSerializer):

    class Meta:
        model = EmpleadoModelo
        fields = ('pk', 'idnum', 'paterno', 'materno', 'nombres', 'fono', 'email', 'ingreso')

class PagoSerializer(ModelSerializer):

    class Meta:
        model = PagoSueldo
        fields = ('empleado', 'sueldobase', 'diastrabajados')

