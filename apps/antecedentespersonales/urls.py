from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.antecedentespersonales.views import AntecedentesPersonalesList, AntecedentesPersonalesCreate, AntecedentesPersonalesUpdate, AntecedentesPersonalesDelete

urlpatterns = [
    url(r'^$', login_required(AntecedentesPersonalesList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(AntecedentesPersonalesCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(AntecedentesPersonalesUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(AntecedentesPersonalesDelete.as_view()), name='eliminar'),
]