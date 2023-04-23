from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0,blank=True, null=True, verbose_name='Cantidad')

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Prueba'
        verbose_name_plural = 'Pruebas'
        ordering = ['titulo']