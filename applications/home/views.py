from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

from .models import Blog
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from applications.home.models import Blog

def formulario_contactar(request):
    print("Formulario de contactar")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        message = "Nombre: " + name + " Email: " + email + " Tel: " + phone + " Mensaje: " + message
        
        print(name, email, phone, message)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['euskodev@gmail.com','retegi84@gmail.com','olvind78@gmail.com']
        send_mail(email, message, from_email, recipient_list)
        messages.add_message(request, messages.INFO, "Hemos recibido el email, en breve nos pondremos en contacto. | Emaila jaso dugu, laster harremanetan jarriko gara.")

    return render(request, "home/index.html")

class HomePageView(ListView):
    template_name = "home/index.html"
    model = Blog
    context_object_name = 'entradas_blog'
    def get_queryset(self):
        # Obtenemos el queryset original
        queryset = super().get_queryset()
        # Filtramos y seleccionamos el primer objeto
        first_item = queryset.first()
        # Si no hay objetos en el queryset, devolvemos un queryset vacío
        if first_item is None:
            return queryset.none()
        # Devolvemos un queryset que contiene solo el primer objeto
        return queryset.order_by('-id')[:3]


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

class LaMaisonDuBordeauxView(TemplateView):
    template_name = "portfolio/la-maison-du-bordeaux/index.html"

class LaMaisonDuBordeauxAproposView(TemplateView):
    template_name = "portfolio/la-maison-du-bordeaux/about.html"

class LaMaisonDuBordeauxProduitsView(TemplateView):
    template_name = "portfolio/la-maison-du-bordeaux/products.html"

class LaMaisonDuBordeauxBoutiqueView(TemplateView):
    template_name = "portfolio/la-maison-du-bordeaux/store.html"

class SunAndSurfView(TemplateView):
    template_name = "portfolio/sun-and-surf/index.html"

class DeMiTierraView(TemplateView):
    template_name = "portfolio/de-mi-tierra/index.html"

class LaFortunaTripView(TemplateView):
    template_name = "portfolio/la-fortuna-trip/index.html"

class DeMiTierrapView(TemplateView):
    template_name = "portfolio/de-mi-tierra/index.html"





