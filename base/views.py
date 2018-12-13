
# Django
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, TemplateView, FormView

# Locales:
from fuente import base, email, encriptado, paises, mobile
from .var import *
from .links import links
from .models import *



CONTEXT = {}
CONTEXT.update(VAR)
CONTEXT["links"] = links
CONTEXT["conf"] = Configuration()
CONTEXT["IMAGE"] = IMG_LOGO



class IndexView(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = ""
        context["subtitleimg"] = IMG_HOME
        return context

    def dispatch(self, request):
        # Detecta si es un dispositivo mobil y obtiene la ruta de la plantilla 
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)


    


class PoliticaDePrivacidadView(TemplateView):
    template_name = "base/politica_de_privacidad.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Política de privacidad")
        context["subtitleimg"] = IMG_DEFAULT
        return context

    def dispatch(self, request):
        # Detecta si es un dispositivo mobil y obtiene la ruta de la plantilla 
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)