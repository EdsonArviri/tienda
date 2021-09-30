from django import forms
from django .forms import ModelForm

from . import models
class DateInput(forms.DateInput):
    input_type='date'

class LocalidadForm(ModelForm):
    class Meta:
        model=models.Localidad
        fields='__all__'

class PersonaForm(ModelForm):
    class Meta:
        model=models.Persona
        fields='__all__'
        widgets={
            'num_doc':forms.TextInput(attrs={'type':'number','class':'form-control input'}),
            'apellido':forms.TextInput(attrs={'class':'form-control input','text-transform':'capitalize',
                        'placeholder':'Apellido de la persona'}),
            'nombre':forms.TextInput(attrs={'class':'form-control input','text-transform':'capitalize'}),
            'fecha_nac':DateInput(format='%Y-%m-%d',attrs={'class':'form-control input-sm'}),
            'telefono':forms.NumberInput(attrs={'class':'form-control input'}),
            'localidad':forms.Select(attrs={'class':'form-control input'})

        }
       


