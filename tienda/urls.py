
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('nueva_persona',views.nueva_persona,name='nueva_persona'),
    path('agregar_localidad',views.nueva_localidad,name='nueva_localidad'),
    path('listar_personas',views.listar_personas,name='listar_personas'),
    path('modificar_persona/<int:pk>',views.modificar_persona,name='persona_modificar'),
    path('eliminar_persona/<int:pk>',views.eliminar_persona,name='persona_eliminar')

]