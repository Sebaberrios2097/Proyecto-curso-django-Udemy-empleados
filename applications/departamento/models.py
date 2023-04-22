from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre corto', max_length=20, blank=True, unique=True)
    anulate = models.BooleanField('Anulado', default=False)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' | ' + self.shor_name
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']
        unique_together = ('name', 'shor_name')