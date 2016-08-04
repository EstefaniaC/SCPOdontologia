from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.interconsulta.views import InterconsultaList, InterconsultaCreate, InterconsultaUpdate, InterconsultaDelete

urlpatterns = [
    url(r'^$', login_required(InterconsultaList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(InterconsultaCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(InterconsultaUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(InterconsultaDelete.as_view()), name='eliminar'),
]
