from django.db import models

# Create your models here.

class EmpleadoModelo(models.Model):
    idnum = models.IntegerField()
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    ingreso = models.IntegerField()

    def __str__(self):
        return self.nombres+' '+self.paterno+' '+self.materno


class PagoSueldo(models.Model):
    empleado = models.ForeignKey(EmpleadoModelo, null=False, blank=False, on_delete=models.CASCADE)
    sueldobase = models.IntegerField()
    diastrabajados = models.IntegerField()

    def __str__(self):
        return self.empleado.nombres
