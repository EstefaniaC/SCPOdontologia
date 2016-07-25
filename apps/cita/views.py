from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.cita.models import Cita
from apps.cita.forms import CitaForm

# Create your views here.


class CitaList(ListView):
    model = Cita
    template_name = "cita/cita_list.html"

    def get_queryset(self):
        queryset = Cita.objects.filter(activo=True).order_by('id') #Cita.objects.all().order_by('fecha', 'hora')
        return queryset


class CitaCreate(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = "cita/cita_create.html"
    success_url = reverse_lazy("cita:listar")


class CitaUpdate(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = "cita/cita_create.html"
    success_url = reverse_lazy("cita:listar")


class CitaDelete(DeleteView):
    model = Cita
    template_name = "cita/cita_delete.html"
    success_url = reverse_lazy("cita:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class CitaCancel(DeleteView):
    model = Cita
    template_name = "cita/cita_cancel.html"
    success_url = reverse_lazy("cita:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.cancelada = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
