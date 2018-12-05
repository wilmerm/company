
# Django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, TemplateView, FormView

# Módulos locales
from base.var import *
from base.links import links
from base.models import Configuration
from fuente.base import Texto, Numero, Fecha
from fuente.email import Email
from .models import *
from .forms import *


CONTEXT = {}
CONTEXT.update(VAR)
CONTEXT["links"] = links
CONTEXT["conf"] = Configuration()




class IndexView(TemplateView):
    template_name = "prestamos/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Préstamos")
        context["subtitleimg"] = IMG_PRESTAMOS
        return context
    



class SolicitudView(FormView):
    template_name = "prestamos/solicitud.html"
    form_class = SolicitudForm
    success_url = reverse_lazy("prestamos_solicitud_enviada")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Solicitar préstamo")
        context["subtitleimg"] = IMG_PRESTAMOS_SOLICITUD
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    


class SolicitudEnviadaView(TemplateView):
    template_name = "prestamos/solicitud_enviada.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("¡Solicitud enviada!")
        context["subtitleimg"] = IMG_PRESTAMOS_SOLICITUD
        return context




class CalculadoraView(TemplateView):
    template_name = "prestamos/calculadora.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Calculadora de préstamos")
        context["subtitleimg"] = IMG_PRESTAMOS_CALCULADORA
        return context
