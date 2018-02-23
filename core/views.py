import datetime
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Promocao
from mozi.models import Mozix
from pet.models import Petmania
from mcdonalds.models import Mcdonalds
from acai.models import Acai

def index(request):
	#no posts, posso fazer no models um campo para data limite de exibicao, desta forma crio aqui no views a condicao para a exibicao do mesmo.
	posts = Promocao.objects.filter(encerramento__lte=timezone.now()).order_by('-encerramento')
	mozis = Mozix.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]#usar o filtro manipulando o timezone é uma boa, exibir valores postados na ultima semana
	petmanias = Petmania.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]
	mcs = Mcdonalds.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]
	acais = Acai.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))[0:3]
	return render(request, 'core/index.html', {'posts': posts, 'mozis': mozis, 'petmanias': petmanias, 'mcs': mcs, 'acais': acais})

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