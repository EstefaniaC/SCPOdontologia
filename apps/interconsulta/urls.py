from django.conf.urls import include, url
from django.contrib import admin

from apps.interconsulta.views import InterconsultaList, InterconsultaCreate, InterconsultaUpdate, InterconsultaDelete

urlpatterns = [
    url(r'^$', InterconsultaList.as_view(), name="listar"),
    url(r'^nuevo$', InterconsultaCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', InterconsultaUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', InterconsultaDelete.as_view(), name='eliminar'),
]
