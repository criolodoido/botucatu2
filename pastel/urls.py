from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='pastel'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),#mudancas aqui"
	url(r'^cardapio$', views.cardapio, name='cardapio'),
	url(r'^fabricacao$', views.fabricacao, name='fabricacao'),
	url(r'^cupons$', views.cupons, name='cupons'),
	]