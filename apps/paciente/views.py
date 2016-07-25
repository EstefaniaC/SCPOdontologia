from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.paciente.models import Paciente
from apps.paciente.forms import PacienteForm

# Create your views here.


class PacienteList(ListView):
    model = Paciente
    template_name = "paciente/paciente_list.html"

    def get_queryset(self):
        queryset = Paciente.objects.filter(activo=True).order_by('id')
        return queryset


class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "paciente/paciente_create.html"
    success_url = reverse_lazy("paciente:listar")


class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "paciente/paciente_create.html"
    success_url = reverse_lazy("paciente:listar")


class PacienteDelete(DeleteView):
    model = Paciente
    template_name = "paciente/paciente_delete.html"
    success_url = reverse_lazy("paciente:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
