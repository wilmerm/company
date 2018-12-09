
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


CONTEXT = {}
CONTEXT.update(VAR)
CONTEXT["links"] = links
CONTEXT["conf"] = Configuration()
CONTEXT["IMAGE"] = IMG_LOGO 





class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Blog")
        context["subtitleimg"] = IMG_BLOG
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "articulos,publicaciones,noticias,informaciones"
        return context

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)





class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = _("Artículos del blog")
        context["subtitleimg"] = IMG_BLOG
        context["IMAGE"] = context["subtitleimg"]
        context["KEYWORDS"] = "articulos,publicaciones,noticias,informaciones"
        return context

    def dispatch(self, request):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request)






class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT)
        context["subtitle"] = str(self.object)
        context["subtitleimg"] = IMG_BLOG_ARTICLE
        context["IMAGE"] = self.object.GetImg()
        context["KEYWORDS"] = self.object.GetTags()
        context["TITLE"] = self.object.title
        context["DESCRIPTION"] = self.object.description[:200]
        # Conteo de visitas a este artículo.
        self.object.visitas = self.object.visitas + 1
        self.object.save()
        return context

    def dispatch(self, request, pk=None, slug=None):
        self.template_name = mobile.getTemplate(request, self.template_name)
        return super().dispatch(request, pk, slug)

