# Python
import os
import datetime

# Django.
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.template import defaultfilters

# Módulos locales
from base.var import *
from base.models import Configuration
from fuente.base import Texto, Numero, Fecha
from fuente.email import Email









class Post(models.Model):
    """Modelo de base de datos para la publicación de nuevos articulos
    en venta para la tienda.
    """
    title = models.CharField(_("Título"), max_length=100)
    content = models.TextField(_("Contenido"), blank=True)
    description = models.TextField(_("Descripción"), blank=True)
    tags = models.CharField(_("Etiquetas"), max_length=100, blank=True)
    active = models.BooleanField(_("¿Disponible?"), default=True)
    img_width = models.PositiveIntegerField(blank=True, editable=False)
    img_height = models.PositiveIntegerField(blank=True, editable=False)
    img = models.ImageField(_("Imágen"), width_field="img_width", height_field="img_height", upload_to="tienda/post/%Y/%m/")
    pub_date = models.DateTimeField(_("Fecha de publicación"), auto_now_add=True)
    slug = models.SlugField(max_length=100, blank=True, editable=False, unique=True)

    class Meta:
        verbose_name = _("Publicación")
        verbose_name_plural = _("Publicaciones")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify("{}-pub-{}".format(self.title, self.pk))
        super().save(*args, **kwargs)

    def GetImg(self):
        if not self.img:
            return IMG_TIENDA_POST
        return self.img.url

    def GetTags(self):
        if not self.tags:
            self.tags = self.slug.replace("-", ",")
        return self.tags

    def Url(self):
        return reverse_lazy("tienda_post_detail", kwargs={"slug": self.slug})