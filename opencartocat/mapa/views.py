# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response



# Definim la pagina del nostre projecte
def mapa(request):
 return render_to_response('base.html')

