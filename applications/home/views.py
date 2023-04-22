from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba

# Create your views here.

class indexView(TemplateView):
    template_name = 'home/home.html'

class pruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['1','2','3','4','5','6','7','8','9','10']
    context_object_name = 'lista_prueba'


class modeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = 'tabla_prueba'


