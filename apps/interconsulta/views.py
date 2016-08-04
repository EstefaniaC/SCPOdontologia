from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.interconsulta.models import Interconsulta
from apps.interconsulta.forms import InterconsultaForm

# Create your views here.

class InterconsultaList(ListView):
    model = Interconsulta
    paginate_by = 25
    template_name = "interconsulta/interconsulta_list.html"

    def get_queryset(self):
        queryset = Interconsulta.objects.filter(activo=True).order_by('id')
        return queryset


class InterconsultaCreate(CreateView):
    model = Interconsulta
    form_class = InterconsultaForm
    template_name = "interconsulta/interconsulta_create.html"
    success_url = reverse_lazy("interconsulta:listar")


class InterconsultaUpdate(UpdateView):
    model = Interconsulta
    form_class = InterconsultaForm
    template_name = "interconsulta/interconsulta_create.html"
    success_url = reverse_lazy("interconsulta:listar")


class InterconsultaDelete(DeleteView):
    model = Interconsulta
    template_name = "interconsulta/interconsulta_delete.html"
    success_url = reverse_lazy("interconsulta:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
