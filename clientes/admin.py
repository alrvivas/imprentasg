from django.contrib import admin
from .models import Empresa,Representante

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre','rfc')


@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre','apellidos','empresa')

