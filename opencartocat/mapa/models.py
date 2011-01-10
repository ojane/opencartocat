# Create your models here.

from django.contrib.gis.db import models

class mapa(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    nom = models.CharField(max_length=50)
    area = models.IntegerField()
    descripcio = models.CharField(max_length=50)
    localita = models.CharField(max_length=50)
    poblacio = models.IntegerField()
    regio = models.CharField(max_length=50)
    subregio = models.CharField(max_length=50)
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = "Dades Municipis"

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name
