from django.shortcuts import render
from App.models import futbolista
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

# Create your views here.

def index(request):
    return render(request, 'App/index.html')

class FutbolistaList(ListView):
    model = futbolista

class FutbolistaCrear(CreateView):
  model = futbolista
  success_url = "/panel-futbolista"
  fields = ["nombre", "equipo", "edad"]

class FutbolistaBorrar(DeleteView):
    model = futbolista
    success_url = "/panel-futbolista"

class FutbolistaUpdate(UpdateView):
    model = futbolista
    success_url = "/panel-futbolista"
    fields = ["nombre", "equipo", "edad"]









