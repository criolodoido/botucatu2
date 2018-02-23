from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='mcdonalds'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),#mudancas aqui"
	url(r'^oferta$', views.oferta, name='oferta'),
	url(r'^combos$', views.combos, name='combos'),
	url(r'^cafe$', views.cafe, name='cafe'),
	url(r'^sorvete$', views.sorvete, name='sorvete'),
	url(r'^cupons$', views.cupons, name='cupons'),
	]