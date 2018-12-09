
# Django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, TemplateView, FormView

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
    template_name = "tienda/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Tienda")
        context["subtitleimg"] = IMG_TIENDA
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "tienda,online,en linea,venta,compra"
        return context

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)





class PostListView(ListView):
    model = Post
    template_name = "tienda/post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Publicaciones")
        context["subtitleimg"] = IMG_TIENDA_POST
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "tienda,online,en linea,venta,compra"
        return context

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)





class PostDetailView(DetailView):
    model = Post 
    template_name = "tienda/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _(self.object.title)
        context["subtitleimg"] = IMG_TIENDA_POST
        context["IMAGE"] = self.object.GetImg()
        context["KEYWORDS"] = self.object.GetTags()
        context["TITLE"] = self.object.title
        context["DESCRIPTION"] = self.object.description[:200]
        return context

    def dispatch(self, request, pk=None, slug=None):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request, pk, slug)