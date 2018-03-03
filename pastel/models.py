# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Pastelaria(models.Model):
	TIPOS = (
		('CUPOM', 'Cupons'),
		('CARD', 'Cardápio'),
		('FABR', 'Fabricação Própria'),
		('INI', 'Inicial')
	)

	tipos = models.CharField(max_length=6, choices=TIPOS, null=False)
	titulo = models.CharField(max_length=100, null=False, blank=False)
	apresentacao = models.TextField()
	imagem = CloudinaryField('imagem', null=False, blank=False)
	validade = models.DateField(null=False, blank=False)
	datapublicacao = models.DateField(null=False, blank=False)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		#return reverse("detalhe", kwargs={"pk": self.pk})
		return "post/%s" %(self.pk)