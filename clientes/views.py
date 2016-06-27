# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Avg,Sum
from django.views.generic.base import View
from models import *
from forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  

def LoginView(request):
    if not request.user.is_anonymous():
        return redirect('index')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('index')
                else:
                    return render_to_response('inactivousuario.html', context_instance=RequestContext(request))#no activo
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))#no usuario
    else:
        formulario = AuthenticationForm()
    page_title = "Ingreso de Usuarios"
    return render_to_response('login.html',{'formulario':formulario,'page_title':page_title}, context_instance=RequestContext(request))

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def index(request):
    page_title = "Imprenta SC"
    user = request.user    
    template_name ="index.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 


@login_required(login_url='/login/')
def add_empresa(request):
    page_title = "Añadir Empresa"
    user = request.user
    empresa = Empresa.objects.all()
    if request.method == 'POST':
        form_empresa = empresaForm(request.POST,request.FILES)
        if form_empresa.is_valid():
            empresa = form_empresa.save(commit = False)
            empresa.save()            
            return redirect(empresa.get_absolute_url())
    else:
        form_empresa = empresaForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-cliente.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def empresas(request):
    page_title = "Empresas"
    user = request.user
    empresas = Empresa.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) | Q(rfc__icontains=query)
        )    
        results = Empresa.objects.filter(qset).order_by('-id')
        template_name = "resultados-cliente.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="clientes.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def empresa(request,empresa_id):
    user = request.user
    empresa = get_object_or_404(Empresa, id=empresa_id)
    #ordenes_pendientes = Orden.objects.filter(empresa=empresa).exclude(estatus_cobranza=2).order_by('-id')[:5]
    #ordenes_pagadas = Orden.objects.filter(empresa=empresa,estatus_cobranza=2).order_by('-id')[:5]
    page_title = empresa.nombre     
    template_name ="cliente.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_empresa(request,empresa_id):
    page_title = "Editat Empresa"
    user = request.user
    empresa = get_object_or_404(Empresa, id=empresa_id)
    if request.method == 'POST':
        form_empresa = empresaForm(request.POST,request.FILES,instance=empresa)
        if form_empresa.is_valid():
            empresa = form_empresa.save(commit = False)
            empresa.save()            
            return redirect(empresa.get_absolute_url())
    else:
        form_empresa = empresaForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-cliente.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ordenes_pendientes_empresa(request,empresa_id):
    user = request.user
    empresa = get_object_or_404(Empresa, id=empresa_id)
    ordenes_pendientes = Orden.objects.filter(empresa=empresa).exclude(estatus_cobranza=2).order_by('-id')
    page_title = "Ordenes"        
    template_name ="ordenes-pendientes-cliente.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ordenes_pagadas_empresa(request,empresa_id):
    user = request.user
    empresa = get_object_or_404(Cliente, id=empresa_id)
    ordenes_pagadas = Orden.objects.filter(empresa=empresa,estatus_cobranza=2).order_by('-id')
    page_title = "Ordenes"        
    template_name ="ordenes-pagadas-cliente.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))


@login_required(login_url='/login/')
def add_representante(request):
    page_title = "Añadir Representante"
    user = request.user
    empresas = Empresa.objects.all()
    representante = Representante.objects.all()
    if request.method == 'POST':
        form_representante = representanteForm(request.POST,request.FILES)
        if form_representante.is_valid():
            representante = form_representante.save(commit = False)
            representante.save()            
            return redirect(representante.get_absolute_url())
    else:
        form_representante = representanteForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-representante.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def representantes(request):
    page_title = "Representantes"
    user = request.user
    representante = Representante.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) | Q(rfc__icontains=query)
        )    
        results = Representante.objects.filter(qset).order_by('-id')
        template_name = "resultados-representante.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="representantes.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def representante(request,representante_id):
    user = request.user
    representante = get_object_or_404(Representante, id=representante_id)    
    page_title = representante.nombre     
    template_name ="representante.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_representante(request,representante_id):
    page_title = "Editat Empresa"
    user = request.user
    representante = get_object_or_404(Empresa, id=representante_id)
    if request.method == 'POST':
        form_representante = representanteForm(request.POST,request.FILES,instance=representante)
        if form_representante.is_valid():
            representante = form_representante.save(commit = False)
            representante.save()            
            return redirect(representante.get_absolute_url())
    else:
        form_representante = representanteForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-representante.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))