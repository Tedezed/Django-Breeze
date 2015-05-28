from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import os

admin.autodiscover()
DJ_PROJECT_DIR = os.path.dirname(__file__)
base_dir = os.path.dirname(DJ_PROJECT_DIR)
ruta_estatica = os.path.join(os.path.dirname(base_dir), 'myproject/breeze/static')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #
    #Admin:
    url(r'^admin/', include(admin.site.urls)),
    #
    #Urls para archivos estaticos
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '%s/css/' % ruta_estatica}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '%s/js/' % ruta_estatica}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '%s/img/' % ruta_estatica}),
    url(r'^font/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '%s/font/' % ruta_estatica}),
    url(r'^admin/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '%s/admin/' % ruta_estatica}),
    #
    #Redireccion a urls Breeze:
    #url(r'^breeze/', include('breeze.urls')),
    #
    #Todas las urls para Breeze urls:
    url(r'', include('breeze.urls')),

)
