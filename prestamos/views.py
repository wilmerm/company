
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
from fuente import mobile
from .models import *
from .forms import *


CONTEXT = {}
CONTEXT.update(VAR)
CONTEXT["links"] = links
CONTEXT["conf"] = Configuration()
CONTEXT["IMAGE"] = IMG_LOGO 





class IndexView(TemplateView):
    template_name = "prestamos/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"] = _("Préstamos")
        context["subtitleimg"] = IMG_PRESTAMOS
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "prestamos,personales,hipotecarios"
        return context

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)





class SolicitudView(CreateView):
    model = Solicitud
    template_name = "prestamos/solicitud.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"] = _("Solicitar préstamo")
        context["subtitleimg"] = IMG_PRESTAMOS_SOLICITUD
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "prestamos,solicitud,solicitar"
        return context

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)



class SolicitudView2(FormView):
    """
    !!!!!!!NO ES UTILIZADA!!!!!!!
    """
    template_name = "prestamos/solicitud.html"
    form_class = SolicitudForm
    success_url = reverse_lazy("prestamos_solicitud_enviada")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"] = _("Solicitar préstamo")
        context["subtitleimg"] = IMG_PRESTAMOS_SOLICITUD
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "prestamos,solicitud,solicitar"
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)

    


class SolicitudEnviadaView(TemplateView):
    template_name = "prestamos/solicitud_enviada.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"] = _("¡Solicitud enviada!")
        context["subtitleimg"] = IMG_PRESTAMOS_SOLICITUD
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = ""
        return context

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)



class CalculadoraView(TemplateView):
    template_name = "prestamos/calculadora.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"] = _("Calculadora de préstamos")
        context["subtitleimg"] = IMG_PRESTAMOS_CALCULADORA
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "prestamos,calculadora,amortizacion,tasa,cuota,pagos"
        return context

    def dispatch(self, request):
        # Detecta si es un dispositivo mobil y obtiene la ruta de la plantilla 
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)



class PrestamoCreateView(CreateView):
    """
    Crea un nuevo préstamo.
    """
    template_name = "prestamos/prestamo_create.html"
    model = Prestamo
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"] = _("Nuevo préstamo")
        context["subtitleimg"] = IMG_PRESTAMOS
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "prestamo"
        return context

    def dispatch(self, request):
        # Detecta si es un dispositivo mobil y obtiene la ruta de la plantilla 
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)