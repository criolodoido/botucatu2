# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Sandubas(models.Model):
	TIPOS = (
		('HOTDOG', 'Lanches e Hot-dog'),
		('BARCA', 'Barca'),
		('PFE', 'Pratos Executivos'),
		('PORC', 'Porções e Bebidas'),
		('CUPONS', 'Cupons'),
		('INI', 'Inicial')
	)

	tipos = models.CharField(max_length=6, choices=TIPOS, null=False)
	titulo = models.CharField(max_length=100, null=False, blank=False)
	apresentacao = models.TextField()
	imagem = CloudinaryField('imagem', null=False, blank=False)
	validade = models.DateField(null=True, blank=True)#testar a validade assim
	datapublicacao = models.DateField(null=False, blank=False)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		#return reverse("detalhe", kwargs={"pk": self.pk})
		return "post/%s" %(self.pk)