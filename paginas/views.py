from django.views.generic import TemplateView


class VistaPaginaDeInicio(TemplateView):
    template_name = "inicio.html"


class VistaAcercaDe(TemplateView):
    template_name = "acerca_de.html"