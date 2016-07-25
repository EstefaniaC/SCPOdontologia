"""odontologia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from odontologia.views import Index

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^inicio/', include('apps.administrador.urls', namespace="administrador")),
    url(r'^paciente/', include('apps.paciente.urls', namespace="paciente")),
    url(r'^tratamiento/', include('apps.tratamiento.urls', namespace="tratamiento")),
    url(r'^cita/', include('apps.cita.urls', namespace="cita")),
    url(r'^historiaClinica/', include('apps.historiaclinica.urls', namespace="historiaClinica")),
    url(r'^antecedentesFamiliares/', include('apps.antecedentesfamiliares.urls', namespace="antecedentesFamiliares")),
    url(r'^receta/', include('apps.receta.urls', namespace="receta")),
    url(r'^antecedentesPersonales/', include('apps.antecedentespersonales.urls', namespace="antecedentesPersonales")),
    url(r'^interconsulta/', include('apps.interconsulta.urls', namespace="interconsulta")),

]
