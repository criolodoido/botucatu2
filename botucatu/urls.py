from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^app2/', include('pet.urls', namespace='petmania')),
    url(r'^app3/', include('pastel.urls', namespace='pastel')),
    url(r'^acaidavital/', include('acai.urls', namespace='acai')),
    url(r'^sandubaslanches/', include('sandubas.urls', namespace='sandubas')),
]
