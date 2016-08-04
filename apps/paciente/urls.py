from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.paciente.views import PacienteList, PacienteCreate, PacienteUpdate, PacienteDelete

urlpatterns = [
    url(r'^$', login_required(PacienteList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(PacienteCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(PacienteUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(PacienteDelete.as_view()), name='eliminar'),
]
