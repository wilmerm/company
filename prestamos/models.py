# Python
import os
import datetime

# Django.
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings

# Módulos locales
from base.var import *
from base.models import Configuration
from fuente.base import Texto, Numero, Fecha, PrestamoBase
from fuente.email import Email
from contabilidad.models import Cuenta
from clientes.models import Cliente







class Solicitud(models.Model, Texto):
    """Crea solicitudes para préstatmos nuevos.
    """
    nombre = models.CharField(_("Nombres y apellidos"), max_length=50, help_text=_("Indíquenos su nombre completo."))
    cedula = models.CharField(_("Cédula"), max_length=20, help_text=_("Indíquenos su número de cédula."))
    telefono = models.CharField(_("Teléfono celular"), max_length=20, help_text=_("Indíquenos su número de teléfono movil."))
    email = models.EmailField(_("Correo electrónico"), max_length=254, blank=True, help_text=_("Indíquenos su correo electrónico."))
    nota = models.TextField(_("Comentario adicional"), blank=True)
    consentimiento = models.BooleanField(_("Estoy de acuerdo"), help_text=_("Declaro haber leído la política de privacidad, y estar de acuerdo con ella."))
    fecha = models.DateTimeField(_("Fecha"), auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, editable=False, help_text=_("Usuario que registró la solicitud (opcional)"))
    
    # Datos extra según pedido de la Empresa.
    direccion = models.CharField(_("Dirección"), max_length=200, help_text=_("Dirección de su residencia o domicilio."))
    estado_civil = models.CharField(_("Estado civil"), max_length=10, choices=ESTADO_CIVIL_CHOICES)
    trabajo_nombre = models.CharField(_("Lugar de trabajo"), max_length=50, blank=True)
    trabajo_direccion = models.CharField(_("Dirección del trabajo"), max_length=200, blank=True)
    trabajo_telefono = models.CharField(_("Teléfono del trabajo"), max_length=20, blank=True)
    trabajo_posicion = models.CharField(_("Puesto que ocupa"), max_length=50, help_text=_("Puesto que ocupa dentro de la empresa."), blank=True)
    trabajo_ingresos = models.DecimalField(_("Ingresos mensuales"), max_digits=11, decimal_places=2, blank=True, default=0, help_text=_("Sus ingresos mensuales dentro de la empresa."))
    trabajo_inicio = models.DateField(_("Fecha en que ingresó"), blank=True, null=True, help_text=_("Fecha en que empezó a formar parte de la empresa como empleado."))
    conyugue_nombre = models.CharField(_("Nombre del conyugue"), max_length=50, blank=True)
    conyugue_trabajo_nombre = models.CharField(_("Lugar de trabajo del conyugue"), max_length=50, blank=True)
    conyugue_trabajo_posicion = models.CharField(_("Puesto que ocupa"), max_length=50, blank=True, help_text=_("Puesto que ocupa el conyugue dentro de la empresa."))
    conyugue_trabajo_direccion = models.CharField(_("Dirección del trabajo dle conyugue"), max_length=200, blank=True)
    conyugue_trabajo_telefono = models.CharField(_("Teléfono del trabajo del conyugue"), max_length=20, blank=True)
    conyugue_trabajo_ingresos = models.DecimalField(_("Ingresos mensuales del conyugue"), max_digits=11, decimal_places=2, blank=True, default=0, help_text=_("Sus ingresos mensuales dentro de la empresa."))
    ref1_nombre = models.CharField(_("Nombre"), max_length=50, blank=True)
    ref1_parentesco = models.CharField(_("Parentesco"), max_length=20, blank=True)
    ref1_telefono = models.CharField(_("Teléfono"), max_length=20, blank=True)
    ref1_celular = models.CharField(_("Celular"), max_length=20, blank=True)
    ref1_direccion = models.CharField(_("Dirección"), max_length=200, blank=True)
    ref2_nombre = models.CharField(_("Nombre"), max_length=50, blank=True)
    ref2_parentesco = models.CharField(_("Parentesco"), max_length=20, blank=True)
    ref2_telefono = models.CharField(_("Teléfono"), max_length=20, blank=True)
    ref2_celular = models.CharField(_("Celular"), max_length=20, blank=True)
    ref2_direccion = models.CharField(_("Dirección"), max_length=200, blank=True)
    ref3_nombre = models.CharField(_("Nombre de la empresa"), max_length=50, blank=True)
    ref3_telefono = models.CharField(_("Teléfono"), max_length=20, blank=True)
    ref4_nombre = models.CharField(_("Nombre de la empresa"), max_length=50, blank=True)
    ref4_telefono = models.CharField(_("Teléfono"), max_length=20, blank=True)
    cedula_file = models.FileField(_("Cédula"), upload_to="prestamos/solicitud/%Y/%m/", blank=True, help_text=_("Suba la copia de su cédula."))
    carta_de_trabajo_file = models.FileField(_("Carta de trabajo"), upload_to="prestamos/solicitud/%Y/%m/", blank=True, help_text=_("Suba la carta de trabajo escaneada."))

    class Meta:
        verbose_name = _("Solicitud")
        verbose_name_plural = _("Solicitudes")

    def __str__(self):
        return "{} {}: {}".format(_("Solicitud"), self.id, self.GetNombreCorto())

    def get_absolute_url(self):
        return reverse("prestamos_solicitud_enviada")

    def clean(self):
        """Operación de limpieza para validar los datos antes de guardar.
        """
        # Validamos la cédula ingresada.
        try:
            self.cedula = self.ValidarCedula(self.cedula)
        except BaseException as e:
            raise ValidationError({"cedula": _("¡Ups! Al parecer la cédula no es válida. {}".format(e))})
        # Limpiamos el nombre para que sea en mayuscula.
        self.nombre = self.nombre.upper()
        # El consentimiento es obligatorio.
        if self.consentimiento == False:
            raise ValidationError({"consentimiento": _("Indique que está de acuerdo con la política de privacidad.")})


    def GetNombreCorto(self):
        return self.nombre.split(" ")[0]








    
class Prestamo(models.Model, PrestamoBase):
    """Gestión de préstamos. Aqui se almacenan los préstamos de 
    los diferentes clientes.
    """
    cuenta = models.ForeignKey(Cuenta, verbose_name=_("Cuenta"), blank=True, null=True, default=None, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, verbose_name=_("Cliente"), on_delete=models.CASCADE)
    monto = models.DecimalField(_("Monto"), max_digits=12, decimal_places=2, help_text=_("Monto del préstamo."))
    tasa = models.DecimalField(_("Tasa"), max_digits=5, decimal_places=2)
    cuotas = models.IntegerField(_("Cuotas"))
    periodo = models.CharField(_("Periodo de pagos"), max_length=10, choices=PERIODO_CHOICES)
    cuotas_tipo = models.CharField(_("Tipo de cuotas"), max_length=10, choices=CUOTA_TIPOS)
    fecha_inicio = models.DateField(_("Fecha de inicio"), default=timezone.now)
    fecha_creacion = models.DateTimeField(_("Fecha de creación"), auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)


    class Meta:
        verbose_name = _("Préstamo")
        verbose_name_plural = _("Préstamos")

    
    def __str__(self):
        try:
            return "{} {}".format(_("Préstamo"), self.cuenta.numero)
        except BaseException:
            return "{} {} {}".format("Préstamo", self.cuenta, self.cliente)


    def save(self, *args, **kwargs):
        """
        Método llamado cuando se crea o modifica.
        """
        # Creamos la cuenta. La cuenta debe crearse automáticamente, ya que 
        # es tratada como una cuenta interna para poder llevar a cabo las 
        # operaciones de transacciones. El usuario no tiene que saber esto.
        cuenta = Cuenta()
        cuenta.numero = cuenta.GetNextNumber()
        cuenta.cliente = self.cliente
        cuenta.save() 
        self.cuenta = cuenta
        super().save(*args, **kwargs)

    
