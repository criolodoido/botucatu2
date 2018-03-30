from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^acaidavital/', include('acai.urls', namespace='acai')),
    url(r'^sandubaslanches/', include('sandubas.urls', namespace='sandubas')),
    url(r'^queromais/', include('queromais.urls', namespace='queromais')),
    url(r'^divino/', include('divino.urls', namespace='divino'))
]
