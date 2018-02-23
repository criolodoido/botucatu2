from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^app2/', include('pet.urls', namespace='petmania')),
    url(r'^app1/', include('mozi.urls', namespace='mozix')),
    url(r'^app3/', include('mcdonalds.urls', namespace='mc')),
    url(r'^app4/', include('acai.urls', namespace='acai')),
]
