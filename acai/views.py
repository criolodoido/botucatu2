# -*- coding: utf 8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Acai

def index(request):
	acais = Acai.objects.filter(tipos='INI', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'acai/index.html', {'acais': acais})

def post_detail(request, pk):
    post = get_object_or_404(Acai, pk=pk)
    Acai.objects.get(pk=pk)
    return render(request, 'acai/post_detail.html', {'post': post})

def oferta(request):
	acais = Acai.objects.filter(tipos='OFERT')
	return render(request, 'acai/index.html', {'acais': acais})

def cupons(request):
	acais = Acai.objects.filter(tipos='CUPOM', validade__gte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'acai/index.html', {'acais': acais})
	
def comboa(request):
	acais = Acai.objects.filter(tipos='COMBOA')
	return render(request, 'acai/index.html', {'acais': acais})

def combob(request):
	acais = Acai.objects.filter(tipos='COMBOB')
	return render(request, 'acai/index.html', {'acais': acais})

def bebidas(request):
	acais = Acai.objects.filter(tipos='BEBIDA')
	return render(request, 'acai/index.html', {'acais': acais})
