from django.contrib.gis import admin
from models import mapa

class mapaAdmin(admin.GeoModelAdmin):
    list_display = ['nom', 'area', 'descripcio', 'lon', 'lat']
    search_fields = ['nom']

admin.site.register(mapa, mapaAdmin)


