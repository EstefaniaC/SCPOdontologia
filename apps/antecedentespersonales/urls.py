from django.conf.urls import include, url
from django.contrib import admin

from apps.antecedentespersonales.views import AntecedentesPersonalesList, AntecedentesPersonalesCreate, AntecedentesPersonalesUpdate, AntecedentesPersonalesDelete

urlpatterns = [
    url(r'^$', AntecedentesPersonalesList.as_view(), name="listar"),
    url(r'^nuevo$', AntecedentesPersonalesCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', AntecedentesPersonalesUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', AntecedentesPersonalesDelete.as_view(), name='eliminar'),
]