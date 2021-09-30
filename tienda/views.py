from django.shortcuts import redirect, render
from . import forms
from .models import Persona

def index(request):
    return render(request,'tienda/index.html')

def nueva_localidad(request):
    formmulario=forms.LocalidadForm()
    dato={'form':formmulario}
    return render(request,'tienda/nueva_localidad.html',dato)

def listar_personas(request,template_name='tienda/listar_personas.html'):
    personas=Persona.objects.all()
    dato_personas={'gentes':personas}
    return render(request,template_name,dato_personas)

def nueva_persona(request):
    if request.method=='POST':
        formulario=forms.PersonaForm(request.POST)#guardo cargado de datos
        if formulario.is_valid():
            formulario.save(commit=True)
            return redirect('listar_personas')
        else:
            print(formulario.errors)
    else:
        formulario=forms.PersonaForm()#lo crea vacio, sin datos
    dato={'form':formulario}
    return render (request,'tienda/persona_form.html',dato)#

def modificar_persona(request,pk):
    persona=Persona.objects.get(num_doc=pk)
    formulario=forms.PersonaForm(request.POST or None,instance=persona)
    if request.method=='POST':
        if formulario.is_valid():
            formulario.save(commit=True)
            return redirect('listar_personas')
        else:
            print(formulario.errors)
    else:
        datos={'form':formulario}
        return render (request,'tienda/persona_form.html',datos)

def eliminar_persona(request,pk,template_name='tienda/persona_confirmar_eliminar.html'):
    persona=Persona.objects.get(num_doc=pk)
    if request.method=='POST':
        persona.delete()
        return redirect('listar_personas')
    else:
        dato={'formulario':persona}
        return render(request,template_name,dato)
