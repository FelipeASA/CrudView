from django.urls import path, include

from Apps.vistasJson.views import *

urlpatterns = [
    path('', empleadojson , name='empleadojson'),
    path('jquery/', consumojson , name='consumojson'),
]
