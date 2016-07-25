from django.conf.urls import include, url
from django.contrib import admin

from apps.tratamiento.views import TratamientoList, TratamientoCreate, TratamientoDelete, TratamientoUpdate

urlpatterns = [
    url(r'^$', TratamientoList.as_view(), name="listar"),
    url(r'^nuevo$', TratamientoCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', TratamientoUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', TratamientoDelete.as_view(), name='eliminar'),

]
