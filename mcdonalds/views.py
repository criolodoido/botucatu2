# -*- coding: utf 8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Mcdonalds

def index(request):
	mcs = Mcdonalds.objects.filter(tipos='INI', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'mcdonalds/index.html', {'mcs': mcs})

def post_detail(request, pk):
    post = get_object_or_404(Mcdonalds, pk=pk)
    Mcdonalds.objects.get(pk=pk)
    return render(request, 'mcdonalds/post_detail.html', {'post': post})

def oferta(request):
	mcs = Mcdonalds.objects.filter(tipos='OFERT')
	return render(request, 'mcdonalds/index.html', {'mcs': mcs})

def cupons(request):
	tickets = Mcdonalds.objects.filter(tipos='CUPOM', validade__gte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'mcdonalds/index.html', {'tickets': tickets})
	
def combos(request):
	mcs = Mcdonalds.objects.filter(tipos='COMBO')
	return render(request, 'mcdonalds/index.html', {'mcs': mcs})

def cafe(request):
	mcs = Mcdonalds.objects.filter(tipos='COFFE')
	return render(request, 'mcdonalds/index.html', {'mcs': mcs})

def sorvete(request):
	mcs = Mcdonalds.objects.filter(tipos='ICE')
	return render(request, 'mcdonalds/index.html', {'mcs': mcs})
