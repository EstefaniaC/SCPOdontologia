from django.conf.urls import include, url
from django.contrib import admin

from apps.receta.views import RecetaList, RecetaCreate, RecetaUpdate, RecetaDelete

urlpatterns = [
    url(r'^$', RecetaList.as_view(), name="listar"),
    url(r'^nuevo$', RecetaCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', RecetaUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', RecetaDelete.as_view(), name='eliminar'),
]
