from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

from .models import Blog





class HomePageView(TemplateView):
    template_name = "home/index.html"


class PoliticasdeprivacidadView(TemplateView):
    template_name = "home/Politicas_de_privacidad.html"


class Politicas_de_cookiesView(TemplateView):
    template_name = "home/politicas_de_cookies.html"


class AvisolegalView(TemplateView):
    template_name = "home/Aviso_legal.html"


class BlogView(ListView):
    model = Blog
    template_name = 'home/Blog.html'
    context_object_name = 'entradas_blog'
    ordering = [
        '-fecha_hora'
    ]

class BlogDetailView(DetailView):
    model = Blog # Especifica el modelo Blog
    template_name = 'home/articulo_completo.html' # Define el template "articulo_completo.html"
    context_object_name = 'articulo'

class AteneaGastronomicaView(TemplateView):
    template_name = "portfolio/atenea-gastronomica/index.html"


