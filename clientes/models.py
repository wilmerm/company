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
    identificacion = models.CharField(_("Identificación"), max_length=20, help_text=_("Número del documento de identidad."))
    identificacion_tipo = models.CharField(_("Tipo de identificación"), max_length=10, choices=IDENTIFICACION_CHOICES)

    
    def GetUrl(self):
        return reverse_lazy("login")

