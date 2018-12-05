
# Django
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, TemplateView, FormView

# Locales:
from fuente import base, email, encriptado, paises
from .var import *
from .links import links
from .models import *



CONTEXT = {}
CONTEXT.update(VAR)
CONTEXT["links"] = links
CONTEXT["conf"] = Configuration()



class IndexView(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = ""
        context["subtitleimg"] = IMG_HOME
        return context
    


class PoliticaDePrivacidadView(TemplateView):
    template_name = "base/politica_de_privacidad.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Política de privacidad")
        context["subtitleimg"] = IMG_DEFAULT
        return context