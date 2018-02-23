from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='acai'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),#mudancas aqui"
	url(r'^oferta$', views.oferta, name='oferta'),
	url(r'^comboa$', views.comboa, name='comboa'),
	url(r'^combob$', views.combob, name='combob'),
	url(r'^bebidas$', views.bebidas, name='bebidas'),
	url(r'^cupons$', views.cupons, name='cupons'),
	]