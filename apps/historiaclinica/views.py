from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.historiaclinica.models import HistoriaClinica
from apps.historiaclinica.forms import HistoriaClinicaForm

# Create your views here.


class HistoriaClinicaList(ListView):
    model = HistoriaClinica
    paginate_by = 25
    template_name = "historiaClinica/historiaClinica_list.html"

    def get_queryset(self):
        queryset = HistoriaClinica.objects.filter(activo=True).order_by('id')
        return queryset


class HistoriaClinicaCreate(CreateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = "historiaClinica/historiaClinica_create.html"
    success_url = reverse_lazy("historiaClinica:listar")


class HistoriaClinicaUpdate(UpdateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = "historiaClinica/historiaClinica_create.html"
    success_url = reverse_lazy("historiaClinica:listar")


class HistoriaClinicaDelete(DeleteView):
    model = HistoriaClinica
    template_name = "historiaClinica/historiaClinica_delete.html"
    success_url = reverse_lazy("historiaClinica:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
