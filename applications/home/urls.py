from os import name
from django.urls import include, path
from . import views

"""
{% url 'home_app:aviso_legal' %}
{% url 'home_app:politica_de_privacidad' %}
{% url 'home_app:politica_de_cookies' %}


"""

app_name = 'home_app'

urlpatterns = [
    path('',
        views.HomePageView.as_view(),
        name='home',
    ),

     path('Politicas de privacidad',
        views.PoliticasdeprivacidadView.as_view(),
        name='politicas_de_privacidad',
    ),


     path('Aviso legal',
        views.AvisolegalView.as_view(),
        name='aviso_legal',
    ),


    path('Politicas de cookies',
        views.Politicas_de_cookiesView.as_view(),
        name='politicas_de_cookies',
    ),

    path('Blog',
        views.BlogView.as_view(),
        name='blog',
    ),

    
    path('blog/articulo/<int:pk>/',
        views.BlogDetailView.as_view(),
        name='blog-detail'
        
        ),

    path('tinymce/', include('tinymce.urls')),


    path('Atenea Gastronomica',
        views.AteneaGastronomicaView.as_view(),
        name='atenea-gastronomica',
    ),

    path('La Maison du Bordeaux',
        views.LaMaisonDuBordeauxView.as_view(),
        name='la-maison-du-bordeaux',
    ),
    path('La Maison du Bordeaux - Apropos',
        views.LaMaisonDuBordeauxAproposView.as_view(),
        name='la-maison-du-bordeaux-apropos',
    ),
    path('La Maison du Bordeaux - Produits',
        views.LaMaisonDuBordeauxProduitsView.as_view(),
        name='la-maison-du-bordeaux-produits',
    ),
    path('La Maison du Bordeaux - Boutique',
        views.LaMaisonDuBordeauxBoutiqueView.as_view(),
        name='la-maison-du-bordeaux-boutique',
    ),



]