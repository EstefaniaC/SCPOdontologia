from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.administrador.views import Inicio
from apps.cita.views import CitaList, CitaCreate, CitaUpdate, CitaDelete, CitaCancel

urlpatterns = [
    url(r'^$', login_required(CitaList.as_view()), name="listar"),
    url(r'^nueva/', login_required(CitaCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(CitaUpdate.as_view()), name="editar"),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(CitaDelete.as_view()), name='eliminar'),
    url(r'^cancelar/(?P<pk>\d+)$', login_required(CitaCancel.as_view()), name="cancelar"),
    url(r'^reagendar/(?P<pk>\d+)$', login_required(CitaCreate.as_view()), name="reagendar"),
   
]
