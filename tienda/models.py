# Python
import os
import datetime

# Django.
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

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
    description = models.TextField(_("Descripción"), blank=True)
    pubdate = models.DateTimeField(_("Fecha de publicación"), auto_now_add=True)
    active = models.BooleanField(_("¿Disponible?"), default=True)
    img_width = models.PositiveIntegerField(blank=True, editable=False)
    img_height = models.PositiveIntegerField(blank=True, editable=False)
    img = models.ImageField(_("Imágen"), width_field="img_width", height_field="img_height", upload_to="tienda/post/%Y/%m/")

    class Meta:
        verbose_name = _("Publicación")
        verbose_name_plural = _("Publicaciones")

    def __str__(self):
        return self.title

    def GetImg(self):
        if not self.img:
            return IMG_TIENDA_POST
        return self.img.url

    def Url(self):
        return reverse_lazy("tienda_post_detail", kwargs={"pk": self.pk})