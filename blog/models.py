# Python
import os
import datetime

# Django.
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.template import defaultfilters
from django.conf import settings

# Módulos locales
from base.var import *
from base.models import Configuration
from fuente.base import Texto, Numero, Fecha
from fuente.email import Email








class Article(models.Model):
    """Publicación de artículos.
    """
    title = models.CharField(_("Título"), max_length=100)
    content = models.TextField(_("Contenido"), help_text=_("Se acepta código HTML"))
    description = models.TextField(_("Descripción"), blank=True, help_text=_("Descripción de la búsqueda"))
    tags = models.CharField(_("Etiquetas"), max_length=100, blank=True)
    img = models.ImageField(_("Imagen"), blank=True, upload_to="blog/post/%Y/%m/", help_text=_("Imagen que se mostrará junto al título de la publicación"))
    slug = models.SlugField(max_length=100, blank=True, unique=True, editable=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    visitas = models.IntegerField(_("Visitas"), default=0, editable=False, help_text=_("Cantidad de visitas a esta entrada"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name=_("Autor"), null=True, blank=True, editable=True)
    

    class Meta:
        verbose_name = _("Artículo")
        verbose_name_plural = _("Artículos")

    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super().save(*args, **kwargs)

    def GetImg(self):
        if not self.img:
            return IMG_BLOG_ARTICLE
        return self.img.url

    def GetTags(self):
        if not self.tags:
            self.tags = self.slug.replace("-", ",")
        return self.tags

    def GetUrl(self):
        return reverse_lazy("blog_article_detail", kwargs={"slug": self.slug})

    def GetArticulosPopulares(self, limit=10):
        """Obtiene un listado de los artículos con mayor número de visitas.
        """
        return Article.objects.all().order_by("-visitas")[:limit]









    

