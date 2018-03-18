from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='sandubas'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),#mudancas aqui"
	url(r'^hotdog&lanches$', views.hotdog, name='hotdog'),
	url(r'^barca$', views.barca, name='barca'),
	url(r'^pratos$', views.pratos, name='pratos'),
	url(r'^porcoes$', views.porcoes, name='porcoes'),
	url(r'^cupons$', views.cupons, name='cupons'),
	]