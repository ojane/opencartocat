from django.conf.urls.defaults import *
from opencartocat.mapa.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^opencartocat/', include('opencartocat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    # Posem una cioncidencia per a la pagina corresponent al mapa
     ('^mapa/$', mapa),
)
