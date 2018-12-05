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








class Solicitud(models.Model, Texto):
    """Crea solicitudes para préstatmos nuevos.
    """
    nombre = models.CharField(_("Nombres y apellidos"), max_length=50, help_text=_("Indíquenos su nombre completo."))
    cedula = models.CharField(_("Cédula"), max_length=20, help_text=_("Indíquenos su número de cédula."))
    telefono = models.CharField(_("Teléfono celular"), max_length=20, help_text=_("Indíquenos su número de teléfono movil."))
    email = models.EmailField(_("Correo electrónico"), max_length=254, blank=True, help_text=_("Indíquenos su correo electrónico."))
    nota = models.TextField(_("Comentario adicional"), blank=True)
    consentimiento = models.CharField(_("Estoy de acuerdo"), max_length=50, help_text=_("Declaro haber leído la política de privacidad, y estar de acuerdo con ella."))
    fecha = models.DateTimeField(_("Fecha"), auto_now_add=True)

    class Meta:
        verbose_name = _("Solicitud")
        verbose_name_plural = _("Solicitudes")

    def __str__(self):
        return "{} {}: {}".format(self.verbose_name, self.id, self.GetNombreCorto())

    def get_absolute_url(self):
        return reverse("solicitud_detail", kwargs={"pk": self.pk})

    def GetNombreCorto(self):
        return self.nombre.split(" ")[0]








    
