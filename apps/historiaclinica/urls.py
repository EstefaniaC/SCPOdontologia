from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.historiaclinica.views import HistoriaClinicaList, HistoriaClinicaCreate, HistoriaClinicaUpdate, HistoriaClinicaDelete

urlpatterns = [
    url(r'^$', login_required(HistoriaClinicaList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(HistoriaClinicaCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(HistoriaClinicaUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(HistoriaClinicaDelete.as_view()), name='eliminar'),
]
