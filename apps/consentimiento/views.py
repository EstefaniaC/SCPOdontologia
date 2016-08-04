from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.consentimiento.models import Consentimiento
from apps.consentimiento.forms import ConsentimientoForm

# Create your views here.

class ConsentimientoList(ListView):
    model = Consentimiento
    paginate_by = 25
    template_name = "consentimiento/consentimiento_list.html"

    def get_queryset(self):
        queryset = Consentimiento.objects.filter(activo=True).order_by('id')
        return queryset


class ConsentimientoCreate(CreateView):
    model = Consentimiento
    form_class = ConsentimientoForm
    template_name = "consentimiento/consentimiento_create.html"
    success_url = reverse_lazy("consentimiento:listar")


class ConsentimientoUpdate(UpdateView):
    model = Consentimiento
    form_class = ConsentimientoForm
    template_name = "consentimiento/consentimiento_create.html"
    success_url = reverse_lazy("consentimiento:listar")


class ConsentimientoDelete(DeleteView):
    model = Consentimiento
    template_name = "consentimiento/consentimiento_delete.html"
    success_url = reverse_lazy("consentimiento:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
