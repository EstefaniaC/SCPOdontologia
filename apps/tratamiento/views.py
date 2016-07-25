from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.tratamiento.models import Tratamiento
from apps.tratamiento.forms import TratamientoForm
# Create your views here.

 
class TratamientoList(ListView):
    model = Tratamiento
    template_name = "tratamiento/tratamiento_list.html"

    def get_queryset(self):
        queryset = Tratamiento.objects.filter(activo=True).order_by('id')
        return queryset


class TratamientoCreate(CreateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = "tratamiento/tratamiento_create.html"
    success_url = reverse_lazy('tratamiento:listar')


class TratamientoUpdate(UpdateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = "tratamiento/tratamiento_create.html"
    success_url = reverse_lazy('tratamiento:listar')

class TratamientoDelete(DeleteView):
    model = Tratamiento
    template_name = "tratamiento/tratamiento_delete.html"
    success_url = reverse_lazy("tratamiento:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
