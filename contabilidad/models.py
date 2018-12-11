# Python
import os
import datetime

# Django.
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.conf import settings

# Módulos locales
from base.var import *
from base.models import Configuration
from fuente.base import Texto, Numero, Fecha
from fuente.email import Email






class Cuenta(models.Model):
    """Gestión de préstamos. Aqui se almacenan los préstamos de 
    los diferentes clientes.
    """
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Cliente"), on_delete=models.PROTECT, help_text=_("Cliente del préstamo."))
    # Fields automáticas.
    numero = models.CharField(_("Número"), unique=True, max_length=8)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Usuario"), related_name="user", on_delete=models.SET_DEFAULT, editable=False, default=None, help_text=_("Usuario que creó esto."))
    fecha_creacion = models.DateTimeField(_("Fecha de creación"), auto_now_add=True)
    tags = models.CharField(max_length=200)


    class Meta:
        verbose_name = _("Cuenta")
        verbose_name_plural = _("Cuentas")

    
    def __str__(self):
        return "{} {}".format(self.verbose_name, self.numero)
