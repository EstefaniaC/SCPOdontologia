from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.antecedentespersonales.models import AntecedentesPersonales
from apps.antecedentespersonales.forms import AntecedentesPersonalesForm

# Create your views here.

class AntecedentesPersonalesList(ListView):
    model = AntecedentesPersonales
    template_name = "antecedentesPersonales/antecedentesPersonales_list.html"

    def get_queryset(self):
        queryset = AntecedentesPersonales.objects.filter(activo=True).order_by('id')
        return queryset


class AntecedentesPersonalesCreate(CreateView):
    model = AntecedentesPersonales
    form_class = AntecedentesPersonalesForm
    template_name = "antecedentesPersonales/antecedentesPersonales_create.html"
    success_url = reverse_lazy("antecedentesPersonales:listar")


class AntecedentesPersonalesUpdate(UpdateView):
    model = AntecedentesPersonales
    form_class = AntecedentesPersonalesForm
    template_name = "antecedentesPersonales/antecedentesPersonales_create.html"
    success_url = reverse_lazy("antecedentesPersonales:listar")


class AntecedentesPersonalesDelete(DeleteView):
    model = AntecedentesPersonales
    template_name = "antecedentesPersonales/antecedentesPersonales_delete.html"
    success_url = reverse_lazy("antecedentesPersonales:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
