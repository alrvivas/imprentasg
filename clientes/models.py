from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Empresa(models.Model):
	fecha_registro = models.DateField(auto_now_add=True,verbose_name=('Fecha de regidtro'))	
	nombre = models.CharField(max_length=140,null=True)
	activa = models.BooleanField(default=True)
	rfc = models.CharField(max_length=140,null=True,blank=True)
	celular	= models.CharField(max_length=15,null=True,blank=True)
	telefono = models.CharField(max_length=15,null=True)
	dias_credito = models.PositiveIntegerField(null=True)
	imagen = models.ImageField("Imagen Cliente", upload_to="images/clientes", blank=True, null=True,default='images/clientes/default-01.jpg')
	
	@models.permalink
	def get_absolute_url(self):
		return('empresa', (), { 'empresa_id': self.id })
		
	@models.permalink
	def get_absolute_url_edit_e(self):
		return('editar-empresa', (), { 'empresa_id': self.id })

	@models.permalink
	def get_absolute_url_ordenes_pendientes_cliente(self):
		return('ordenes-pendientes-empresa', (), { 'empresa_id': self.id })

	@models.permalink
	def get_absolute_url_ordenes_pagadas_cliente(self):
		return('ordenes-pagadas-empresa', (), { 'empresa_id': self.id })

	def __unicode__(self):
		return unicode(self.nombre)

class Representante(models.Model):
	fecha_registro = models.DateField(auto_now_add=True,verbose_name=('Fecha de registro'))
	principal = models.BooleanField(default=True)	
	nombre = models.CharField(max_length=140,null=True)
	apellidos = models.CharField(max_length=140,null=True)
	celular	= models.CharField(max_length=15,null=True)
	telefono = models.CharField(max_length=15,null=True)	
	empresa = models.ForeignKey(Empresa,null=True, blank=True)
	puesto = models.CharField(max_length=140,null=True)
	imagen = models.ImageField("Imagen Cliente", upload_to="images/clientes/representantes", blank=True, null=True,default='images/clientes/default-01.jpg')
	
	@models.permalink
	def get_absolute_url(self):
		return('representante', (), { 'representante_id': self.id })
		
	@models.permalink
	def get_absolute_url_edit_e(self):
		return('editar-representante', (), { 'representante_id': self.id })

	def __unicode__(self):
		return unicode(self.nombre)
