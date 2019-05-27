from django.urls import path, include

from Apps.empleados.views import *

urlpatterns = [
    path('', home, name='home'),
    path('listar/', listar.as_view(), name='listar'),
    path('crear/', crear.as_view(), name='crear'),
    path('editar/<int:pk>', editar.as_view(), name='editar'), # ahora usamos primary key
    path('eliminar/<int:pk>', eliminar.as_view(), name='eliminar'), # ahora usamos primary key
]
