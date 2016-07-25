from django.conf.urls import include, url
from django.contrib import admin

from apps.paciente.views import PacienteList, PacienteCreate, PacienteUpdate, PacienteDelete

urlpatterns = [
    url(r'^$', PacienteList.as_view(), name="listar"),
    url(r'^nuevo$', PacienteCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', PacienteUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', PacienteDelete.as_view(), name='eliminar'),
]
