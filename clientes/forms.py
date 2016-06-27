#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Empresa, Representante

class empresaForm(ModelForm):
	class Meta:
		model = Empresa
		fields = '__all__'

class representanteForm(ModelForm):
	class Meta:
		model = Representante
		fields = '__all__'
