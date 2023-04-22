from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name
    search_fields = ('first_name', 'last_name', 'departamento__name')
    list_filter = ('job', 'habilidades', 'departamento__name')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)