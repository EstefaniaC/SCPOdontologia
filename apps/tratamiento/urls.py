from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.tratamiento.views import TratamientoList, TratamientoCreate, TratamientoDelete, TratamientoUpdate

urlpatterns = [
    url(r'^$', login_required(TratamientoList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(TratamientoCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(TratamientoUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(TratamientoDelete.as_view()), name='eliminar'),

]
