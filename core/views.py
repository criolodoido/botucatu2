import datetime
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Promocao
from pet.models import Petmania
from acai.models import Acai
from pastel.models import Pastelaria
from sandubas.models import Sandubas
def index(request):
	#no posts, posso fazer no models um campo para data limite de exibicao, desta forma crio aqui no views a condicao para a exibicao do mesmo.
	posts = Promocao.objects.filter(encerramento__gte=timezone.now()).order_by('-encerramento')
	petmanias = Petmania.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]
	pts = Pastelaria.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]
	acais = Acai.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]
	sandubas = Sandubas.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]
	return render(request, 'core/index.html', {'posts': posts, 'petmanias': petmanias, 'pts': pts, 'acais': acais, 'sandubas': sandubas})

def vital(request):
	return render(request, 'core/vital.html', {})

def bairro(request):
	return render(request, 'core/bairro.html', {})

def centro(request):
	return render(request, 'core/centro.html', {})

def domlucio(request):
	return render(request, 'core/domlucio.html', {})

def facaparte(request):
	return render(request, 'core/facaparte.html', {})