from django.db import models

from datetime import datetime



class Localidad(models.Model):
    nombre=models.CharField(max_length=50)
    cp=models.CharField(max_length=15)
    class Meta:
        ordering=['nombre']
        verbose_name_plural='localidades'
    
    def __str__(self):
        return '%s CP:%s' %(self.nombre,self.cp)

class Persona(models.Model):
    num_doc=models.CharField('N de documento ',max_length=20,primary_key=True)
    apellido=models.CharField(max_length=70)
    nombre=models.CharField('Nombre/s' ,max_length=100)
    fecha_nac= models.DateField('Fecha de  nacimiento',default=datetime.now)
    telefono=models.IntegerField(default=10000)
    localidad=models.ForeignKey(Localidad,null=True,
        blank=True, 
        on_delete=models.PROTECT,
        related_name='persona_localidad'
        )
    '''def __str__(self):
        return '%s - %s , %s'%(self.num_doc,self.apellido,self.nombre)'''

class Cliente(models.Model):
    categoria=models.CharField(max_length=50)
    fecha_alta=models.DateField('Fecha de alta', default=datetime.now)
    persona=models.ForeignKey(Persona,on_delete=models.PROTECT,related_name='cliente_persona')

class Cargo(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150, null=True,blank=True)


class Empleado(models.Model):
    legajo=models.CharField(max_length=60,primary_key=True)
    persona=models.ForeignKey(Persona,on_delete=models.PROTECT,related_name='empleado_persona')
    cargo=models.ForeignKey(Cargo,on_delete=models.PROTECT,related_name='empleado_cargo')

class Articulo(models.Model):
    marca=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150,null=True ,blank=True)
    categoria=models.CharField(max_length=60)
    stock=models.IntegerField(default=0)
    precio=models.FloatField()
    disponible=models.BooleanField('Disponibilidad')

class Movimiento(models.Model):
    numero=models.IntegerField('N de movimiento')
    fecha=models.DateField(default=datetime.now)
    cliente=models.ForeignKey(Cliente,on_delete=models.PROTECT,related_name='movimiento_cliente')

#tabla intermedia

class Item(models.Model):
    articulo=models.ForeignKey(Articulo,on_delete=models.PROTECT,related_name='item_articulo')
    movimiento=models.ForeignKey(Movimiento,on_delete=models.PROTECT,related_name='item_movimiento')
    cantidad=models.IntegerField(default=0)
