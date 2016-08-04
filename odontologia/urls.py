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

#from odontologia.views import Index
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', Index.as_view(), name="index"),
    url(r'^inicio/', include('apps.administrador.urls', namespace="administrador")),
    url(r'^paciente/', include('apps.paciente.urls', namespace="paciente")),
    url(r'^tratamiento/', include('apps.tratamiento.urls', namespace="tratamiento")),
    url(r'^cita/', include('apps.cita.urls', namespace="cita")),
    url(r'^historiaClinica/', include('apps.historiaclinica.urls', namespace="historiaClinica")),
    url(r'^antecedentesFamiliares/', include('apps.antecedentesfamiliares.urls', namespace="antecedentesFamiliares")),
    url(r'^receta/', include('apps.receta.urls', namespace="receta")),
    url(r'^antecedentesPersonales/', include('apps.antecedentespersonales.urls', namespace="antecedentesPersonales")),
    url(r'^interconsulta/', include('apps.interconsulta.urls', namespace="interconsulta")),
    url(r'^consentimiento/', include('apps.consentimiento.urls', namespace="consentimiento")),
    url(r'^usuario/', include('apps.usuario.urls', namespace="usuario")),
    url(r'^accounts/login/', login, {'template_name':'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^reset/password_reset', password_reset, 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    
    url(r'^reset/password_reset_done', password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]
