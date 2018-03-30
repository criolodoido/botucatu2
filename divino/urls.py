from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='divino'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),#mudancas aqui"
	url(r'^cardapio$', views.cardapio, name='cardapio'),
	url(r'^combos$', views.combos, name='combos'),
	url(r'^cupons$', views.cupons, name='cupons'),
	]