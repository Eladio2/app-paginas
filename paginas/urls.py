from django.urls import path
from .views import VistaPaginaDeInicio, VistaAcercaDe

urlpatterns = [
    path("", VistaPaginaDeInicio.as_view(), name="inicio"),
    path("acerca-de/", VistaAcercaDe.as_view(), name="acerca_de"),
]