# -*- coding: utf 8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Queromais

def index(request):
	queromais = Queromais.objects.filter(tipos='INI', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'queromais/index.html', {'queromais': queromais})	

def post_detail(request, pk):
    post = get_object_or_404(Queromais, pk=pk)
    Queromais.objects.get(pk=pk)
    return render(request, 'queromais/post_detail.html', {'post': post})

def cardapio(request):
	queromais = Queromais.objects.filter(tipos='CARD')
	return render(request, 'queromais/index.html', {'queromais': queromais})

def novidades(request):
	queromais = Queromais.objects.filter(tipos='NOVID')
	return render(request, 'queromais/index.html', {'queromais': queromais})
	
def cupons(request):
	tickets = Queromais.objects.filter(tipos='CUPONS')
	return render(request, 'queromais/index.html', {'tickets': tickets})

#modificacao


