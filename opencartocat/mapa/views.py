# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render_to_response

def mapa(request):
 return render_to_response('mapa.html')
