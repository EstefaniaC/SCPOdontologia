from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.receta.models import Receta
from apps.receta.forms import RecetaForm

# Create your views here.

class RecetaList(ListView):
    model = Receta
    paginate_by = 25
    template_name = "receta/receta_list.html"

    def get_queryset(self):
        queryset = Receta.objects.filter(activo=True).order_by('id')
        return queryset


class RecetaCreate(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = "receta/receta_create.html"
    success_url = reverse_lazy("receta:listar")


class RecetaUpdate(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = "receta/receta_create.html"
    success_url = reverse_lazy("receta:listar")


class RecetaDelete(DeleteView):
    model = Receta
    template_name = "receta/receta_delete.html"
    success_url = reverse_lazy("receta:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
