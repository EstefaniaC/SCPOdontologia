from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.antecedentesfamiliares.views import AntecedentesFamiliaresList, AntecedentesFamiliaresCreate, AntecedentesFamiliaresUpdate, AntecedentesFamiliaresDelete

urlpatterns = [
    url(r'^$', login_required(AntecedentesFamiliaresList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(AntecedentesFamiliaresCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(AntecedentesFamiliaresUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(AntecedentesFamiliaresDelete.as_view()), name='eliminar'),
]