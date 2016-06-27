from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', 'clientes.views.index', name='index'),	
	url(r'^login/$', 'clientes.views.LoginView', name='login'),
    url(r'^logout/$', 'clientes.views.LogoutView', name='logout'), 
    url(r'^clientes/', include('clientes.urls')),     
)   

if settings.DEBUG == False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
   )