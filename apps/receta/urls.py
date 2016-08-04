from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.receta.views import RecetaList, RecetaCreate, RecetaUpdate, RecetaDelete

urlpatterns = [
    url(r'^$', login_required(RecetaList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(RecetaCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(RecetaUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(RecetaDelete.as_view()), name='eliminar'),
]
