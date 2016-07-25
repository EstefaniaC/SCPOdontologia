from django.conf.urls import include, url
from django.contrib import admin

from apps.antecedentesfamiliares.views import AntecedentesFamiliaresList, AntecedentesFamiliaresCreate, AntecedentesFamiliaresUpdate, AntecedentesFamiliaresDelete

urlpatterns = [
    url(r'^$', AntecedentesFamiliaresList.as_view(), name="listar"),
    url(r'^nuevo$', AntecedentesFamiliaresCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', AntecedentesFamiliaresUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', AntecedentesFamiliaresDelete.as_view(), name='eliminar'),
]