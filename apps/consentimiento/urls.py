from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.consentimiento.views import ConsentimientoList, ConsentimientoCreate, ConsentimientoUpdate, ConsentimientoDelete

urlpatterns = [
    url(r'^$', login_required(ConsentimientoList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(ConsentimientoCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(ConsentimientoUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(ConsentimientoDelete.as_view()), name='eliminar'),
]