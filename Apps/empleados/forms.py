from django import forms

from Apps.empleados.models import EmpleadoModelo

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = EmpleadoModelo

        fields = ['idnum', 'paterno', 'materno', 'nombres', 'fono', 'email', 'ingreso']

        labels = {
            'idnum':'Numero ID',
            'paterno':'Ap. Paterno',
            'materno':'Ap. Materno',
            'nombres':'Nombres',
            'fono':'Teléfono',
            'email':'E-Mail',
            'ingreso':'Año Ingreso'
        }

        widgets = {
            'idnum':forms.TextInput(), 
            'paterno':forms.TextInput(), 
            'materno':forms.TextInput(), 
            'nombres':forms.TextInput(), 
            'fono':forms.TextInput(), 
            'email':forms.TextInput(), 
            'ingreso':forms.TextInput()
        }

