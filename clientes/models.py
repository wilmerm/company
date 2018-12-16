# Python
import os
import datetime

# Django.
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Módulos locales
from base.var import *
from base.models import Configuration
from fuente.base import Texto, Numero, Fecha
from fuente.email import Email








class User(AbstractUser):
    """
    Modelo para el uso de usuarios. Este modelo reemplaza el 
    modelo User default de django.

    Se hará referencia a él mediante la variable: AUTH_USER_MODEL
    del módulo 'setting' de este proyecto. Ejemplo: 

        user = models.ForeignKey(settings.AUTH_USER_MODEL).

    Debe establecer la variable 'AUTH_USER_MODEL' en el 'setting' 
    de la siguiente manera:

        AUTH_USER_MODEL = 'clientes.User'

    """
    identificacion = models.CharField(_("Identificación"), max_length=20, help_text=_("Número del documento de identidad."))
    identificacion_tipo = models.CharField(_("Tipo de identificación"), max_length=10, choices=IDENTIFICACION_CHOICES)

    
    def GetUrl(self):
        return reverse_lazy("login")






class Cliente(models.Model):
    """
    Modelo para el registro de personas.
    """
    cedula = models.CharField(_("Cédula"), max_length=13, help_text=_("Número de su identificación personal."))
    nombres = models.CharField(_("Nombres"), max_length=100)
    apellidos = models.CharField(_("Apellidos"), max_length=100)
    nacimiento = models.DateField(_("Fecha de nacimiento"), blank=True)
    email = models.EmailField(_("Correo electrónico"), blank=True)
    telefono = models.CharField(_("Teléfono"), max_length=20, blank=True)
    direccion = models.CharField(_("Dirección"), max_length=300, blank=True)
    nota = models.TextField(_("Nota"), blank=True)
    tags = models.CharField(max_length=300)

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")

    def __str__(self):
        return self.GetShortName()

    def GetShortName(self):
        """Obtiene el primer nombre y primer apellido del cliente.
        """
        return "{} {}".format(self.nombres.split(" ")[0], self.apellidos.split(" ")[0])

    
