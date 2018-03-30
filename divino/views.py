# -*- coding: utf 8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Divino

def index(request):
	divinos = Divino.objects.filter(tipos='INI', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'divino/index.html', {'divinos': divinos})

def post_detail(request, pk):
    post = get_object_or_404(Divino, pk=pk)
    Divino.objects.get(pk=pk)
    return render(request, 'divino/post_detail.html', {'post': post})

def cardapio(request):
	divinos = Divino.objects.filter(tipos='CARD')
	return render(request, 'divino/index.html', {'divinos': divinos})

def combos(request):
	divinos = Divino.objects.filter(tipos='COMBOS')
	return render(request, 'divino/index.html', {'divinos': divinos})

def cupons(request):
	tickets = Divino.objects.filter(tipos='CUPOM', validade__gte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'divino/index.html', {'tickets': tickets})
	
