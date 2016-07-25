from django.conf.urls import include, url
from django.contrib import admin

from apps.administrador.views import Inicio
from apps.cita.views import CitaList, CitaCreate, CitaUpdate, CitaDelete, CitaCancel

urlpatterns = [
    url(r'^$', CitaList.as_view(), name="listar"),
    url(r'^nueva/', CitaCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', CitaUpdate.as_view(), name="editar"),
    url(r'^eliminar/(?P<pk>\d+)$', CitaDelete.as_view(), name='eliminar'),
    url(r'^cancelar/(?P<pk>\d+)$', CitaCancel.as_view(), name="cancelar"),
    url(r'^reagendar/(?P<pk>\d+)$', CitaCreate.as_view(), name="reagendar"),
   
]
