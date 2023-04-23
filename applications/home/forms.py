from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):
    # titulo = forms.CharField(max_length=50)
    # subtitulo = forms.CharField(max_length=50)

    class Meta:
        model = Prueba
        fields = [
            'titulo',
            'subtitulo',
            'cantidad',
        ]
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el titulo',
                }
            )
        }
        labels = {
            'titulo': 'Titulo',
            'subtitulo': 'Subtitulo',
            'cantidad': 'Cantidad',
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un valor mayor a 10')
        return cantidad 
        

