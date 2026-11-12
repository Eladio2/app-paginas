from django.test import SimpleTestCase
from django.urls import reverse


class PruebasPaginaInicio(SimpleTestCase):
    def test_direccion(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_url(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertTemplateUsed(respuesta, "inicio.html")

    def test_contenido(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "<h1>Página de inicio</h1>")


class PruebasPaginaAcercaDe(SimpleTestCase):
    def test_direccion(self):
        respuesta = self.client.get("/acerca-de/")
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_url(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertTemplateUsed(respuesta, "acerca_de.html")

    def test_contenido(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertContains(respuesta, "<h1>Página Acerca de</h1>")