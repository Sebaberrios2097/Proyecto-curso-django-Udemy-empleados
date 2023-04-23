from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView)
#models
from applications.empleados.models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    model = Empleado


class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):

        area = self.kwargs['shorname'] #Se recupera el dato ingresado en URL
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista

class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_emp = self.request.GET.get('kwordhab', '')
        empleado = Empleado.objects.get(id = id_emp) 
        return empleado.habilidades.all()
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_view.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/crear_empleado.html"
    fields = ['first_name', 
              'last_name', 
              'job', 
              'departamento',
              'habilidades'
    ]
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        #Logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name', 
            'last_name', 
            'job', 
            'departamento',
            'habilidades'
    ]
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**************Metodo POST**************')
        
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #Logica del proceso
        print('**************Metodo form_valid**************')
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')
