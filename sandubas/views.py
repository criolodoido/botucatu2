# -*- coding: utf 8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Sandubas

def index(request):
	sandubas = Sandubas.objects.filter(tipos='INI', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'sandubas/index.html', {'sandubas': sandubas})	

def post_detail(request, pk):
    post = get_object_or_404(Sandubas, pk=pk)
    Sandubas.objects.get(pk=pk)
    return render(request, 'sandubas/post_detail.html', {'post': post})

def hotdog(request):
	sandubas = Sandubas.objects.filter(tipos='HOTDOG')
	return render(request, 'sandubas/index.html', {'sandubas': sandubas})

def barca(request):
	sandubas = Sandubas.objects.filter(tipos='BARCA')
	return render(request, 'sandubas/index.html', {'sandubas': sandubas})
	
def pratos(request):
	sandubas = Sandubas.objects.filter(tipos='PFE')
	return render(request, 'sandubas/index.html', {'sandubas': sandubas})

def porcoes(request):
	sandubas = Sandubas.objects.filter(tipos='PORC')
	return render(request, 'sandubas/index.html', {'sandubas': sandubas})

def cupons(request):
	sandubas = Sandubas.objects.filter(tipos='CUPONS')
	return render(request, 'sandubas/index.html', {'sandubas': sandubas})

#modificacao


