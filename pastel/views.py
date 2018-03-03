# -*- coding: utf 8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Pastelaria

def index(request):
	pts = Pastelaria.objects.filter(tipos='INI', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'pastel/index.html', {'pts': pts})

def post_detail(request, pk):
    post = get_object_or_404(Pastelaria, pk=pk)
    Pastelaria.objects.get(pk=pk)
    return render(request, 'pastel/post_detail.html', {'post': post})

def cardapio(request):
	pts = Pastelaria.objects.filter(tipos='CARD', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'pastel/index.html', {'pts': pts})

def cupons(request):
	tickets = Pastelaria.objects.filter(tipos='CUPOM', validade__gte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'pastel/index.html', {'tickets': tickets})
	
def fabricacao(request):
	pts = Pastelaria.objects.filter(tipos='FABR', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'pastel/index.html', {'pts': pts})
