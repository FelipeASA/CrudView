from django.contrib import admin

from Apps.empleados.models import EmpleadoModelo, PagoSueldo

admin.site.register(EmpleadoModelo)
admin.site.register(PagoSueldo)
