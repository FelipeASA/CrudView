from django.urls import path, include

from Apps.vistasAPI.views import *

urlpatterns= [
	path('', empleadosAPI.as_view(), name="empleadosAPI"),
	path('pago/', pagosueldoAPI.as_view(), name="pagosueldoAPI"),
	path('jquery2/', consumoAPI, name="consumoAPI"),
]