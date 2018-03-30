import datetime
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Promocao
from acai.models import Acai
from sandubas.models import Sandubas
from queromais.models import Queromais
from divino.models import Divino

def index(request):
	#no posts, posso fazer no models um campo para data limite de exibicao, desta forma crio aqui no views a condicao para a exibicao do mesmo.
	posts = Promocao.objects.filter(encerramento__gte=timezone.now()).order_by('-encerramento')
	acais = Acai.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=30)).order_by('-datapublicacao')[0:3]
	sandubas = Sandubas.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=30)).order_by('-datapublicacao')[0:3]
	queromais = Queromais.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=30)).order_by('-datapublicacao')[0:3]
	divino = Divino.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=30)).order_by('-datapublicacao')[0:3]
	return render(request, 'core/index.html', {'posts': posts, 'acais': acais, 'sandubas': sandubas, 'queromais': queromais, 'divino': divino})

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