from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='queromais'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),
	url(r'^cardapio$', views.cardapio, name='cardapio'),
	url(r'^novidades$', views.novidades, name='novidades'),
	url(r'^cupons$', views.cupons, name='cupons'),
	]