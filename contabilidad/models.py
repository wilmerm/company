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
from clientes.models import Cliente





class Cuenta(models.Model):
    """
    Gestión de cuentas. Es una cuenta contable, capaz de 
    que se realicen transacciones con ella.
    """
    cliente = models.ForeignKey(Cliente, verbose_name=_("Cliente"), on_delete=models.PROTECT, blank=True, null=True, default=None, help_text=_("Cliente del préstamo."))
    # Fields automáticas.
    numero = models.CharField(_("Número"), unique=True, max_length=8)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Usuario"), on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, help_text=_("Usuario que creó esto."))
    fecha_creacion = models.DateTimeField(_("Fecha de creación"), auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = _("Cuenta")
        verbose_name_plural = _("Cuentas")


    def __str__(self):
        return "{} {}".format(_("Cuenta"), self.numero)

    def GetLasNumber(self):
        """
        Obtiene el último número de cuenta registrado.
        """
        try:
            return Cuenta.objects.all().order_by("-numero")[0].numero
        except IndexError:
            return str(int(PRIMER_NUMERO_DE_CUENTA) - 1)
        
    def GetNextNumber(self):
        """
        Obtiene el número de cuenta que continua para 
        nuevos registros.
        """
        return str(int(self.GetLasNumber()) + 1)





