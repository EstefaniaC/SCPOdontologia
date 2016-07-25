from django.conf.urls import include, url
from django.contrib import admin

from apps.consentimiento.views import ConsentimientoList, ConsentimientoCreate, ConsentimientoUpdate, ConsentimientoDelete

urlpatterns = [
    url(r'^$', ConsentimientoList.as_view(), name="listar"),
    url(r'^nuevo$', ConsentimientoCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', ConsentimientoUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', ConsentimientoDelete.as_view(), name='eliminar'),
]