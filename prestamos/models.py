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
from fuente.base import Texto, Numero, Fecha, PrestamoBase
from fuente.email import Email
from contabilidad.models import Cuenta







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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=None, editable=False, help_text=_("Usuario que registró la solicitud (opcional)"))

    class Meta:
        verbose_name = _("Solicitud")
        verbose_name_plural = _("Solicitudes")

    def __str__(self):
        return "{} {}: {}".format(self.verbose_name, self.id, self.GetNombreCorto())

    def get_absolute_url(self):
        return reverse("solicitud_detail", kwargs={"pk": self.pk})

    def GetNombreCorto(self):
        return self.nombre.split(" ")[0]








    
class Prestamo(models.Model, PrestamoBase):
    """Gestión de préstamos. Aqui se almacenan los préstamos de 
    los diferentes clientes.
    """
    cuenta = models.ForeignKey(Cuenta, verbose_name=_("Cuenta"), on_delete=models.CASCADE)
    monto = models.DecimalField(_("Monto"), max_digits=12, decimal_places=2, help_text=_("Monto del préstamo."))
    tasa = models.DecimalField(_("Tasa"), max_digits=5, decimal_places=2)
    cuotas = models.IntegerField(_("Cuotas"))
    periodo = models.CharField(_("Periodo de pagos"), max_length=10, choices=PERIODO_CHOICES)
    #cuotas_tipo = models.CharField(_("Tipo de cuotas"), max_length=10, choices=CUOTA_TIPOS)
    fecha_inicio = models.DateField(_("Fecha de inicio"), auto_now=True)
    # Fields automáticas.


    class Meta:
        verbose_name = _("Préstamo")
        verbose_name_plural = _("Préstamos")

    
    def __str__(self):
        return "{} {}".format(self.verbose_name, self.cuenta.numero)
