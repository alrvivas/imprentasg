from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'clientes.views.empresas', name='empresas'),	
	url(r'^empresa/(?P<empresa_id>[-\w]+)$', 'clientes.views.empresa', name='empresa'),
	url(r'^add-empresa/$', 'clientes.views.add_empresa', name='add-empresa'),
	url(r'^editar-empresa/(?P<empresa_id>[-\w]+)$', 'clientes.views.edit_empresa', name='editar-empresa'),
	url(r'^ordenes-pendientes-empresa/(?P<empresa_id>[-\w]+)$', 'clientes.views.ordenes_pendientes_empresa', name='ordenes-pendientes-empresa'),
	url(r'^ordenes-pagadas-empresa/(?P<empresa_id>[-\w]+)$', 'clientes.views.ordenes_pagadas_empresa', name='ordenes-pagadas-empresa'),
	url(r'^$', 'clientes.views.empresas', name='empresas'),	
	url(r'^representante/(?P<representante_id>[-\w]+)$', 'clientes.views.representante', name='representante'),
	url(r'^add-representante/$', 'clientes.views.add_representante', name='add-representante'),
	url(r'^editar-representante/(?P<representante_id>[-\w]+)$', 'clientes.views.edit_representante', name='editar-representante'),
)