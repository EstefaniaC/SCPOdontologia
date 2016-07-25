from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.antecedentesfamiliares.models import AntecedentesFamiliares
from apps.antecedentesfamiliares.forms import AntecedentesFamiliaresForm

# Create your views here.

class AntecedentesFamiliaresList(ListView):
    model = AntecedentesFamiliares
    template_name = "antecedentesFamiliares/antecedentesFamiliares_list.html"

    def get_queryset(self):
        queryset = AntecedentesFamiliares.objects.filter(activo=True).order_by('id')
        return queryset


class AntecedentesFamiliaresCreate(CreateView):
    model = AntecedentesFamiliares
    form_class = AntecedentesFamiliaresForm
    template_name = "antecedentesFamiliares/AntecedentesFamiliares_create.html"
    success_url = reverse_lazy("antecedentesFamiliares:listar")


class AntecedentesFamiliaresUpdate(UpdateView):
    model = AntecedentesFamiliares
    form_class = AntecedentesFamiliaresForm
    template_name = "antecedentesFamiliares/antecedentesFamiliares_create.html"
    success_url = reverse_lazy("antecedentesFamiliares:listar")


class AntecedentesFamiliaresDelete(DeleteView):
    model = AntecedentesFamiliares
    template_name = "antecedentesFamiliares/antecedentesFamiliares_delete.html"
    success_url = reverse_lazy("antecedentesFamiliares:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
