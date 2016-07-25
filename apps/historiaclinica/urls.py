from django.conf.urls import include, url
from django.contrib import admin

from apps.historiaclinica.views import HistoriaClinicaList, HistoriaClinicaCreate, HistoriaClinicaUpdate, HistoriaClinicaDelete

urlpatterns = [
    url(r'^$', HistoriaClinicaList.as_view(), name="listar"),
    url(r'^nuevo$', HistoriaClinicaCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', HistoriaClinicaUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', HistoriaClinicaDelete.as_view(), name='eliminar'),
]
