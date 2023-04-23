from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class indexView(TemplateView):
    template_name = 'home/home.html'
#Esta es una vista basada en clases que hereda de TemplateView. Se llama indexView y se utiliza para renderizar la plantilla 'home/home.html'.


class pruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['1','2','3','4','5','6','7','8','9','10']
    context_object_name = 'lista_prueba'
#Esta es otra vista basada en clases que hereda de ListView. Se llama modeloPruebaListView y utiliza la plantilla 'home/lista_prueba.html'. En lugar de queryset, utiliza el modelo Prueba para obtener los objetos de la base de datos. Al igual que pruebaListView, utiliza context_object_name para darle un nombre al objeto de contexto que contiene los datos de la vista.

class modeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = 'tabla_prueba'
#Esta es otra vista basada en clases que hereda de ListView. Se llama pruebaListView y utiliza la plantilla 'home/lista.html'. También define el queryset como una lista de cadenas que contiene los valores del 1 al 10. context_object_name se utiliza para darle un nombre al objeto de contexto que contiene los datos de la vista.


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'

    