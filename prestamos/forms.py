
import datetime
from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import gettext as _

from fuente.base import Texto, Numero, Fecha
from .models import Solicitud


class SolicitudForm(forms.Form, Texto):
    nombre = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": _("Nombre"), "title": _("Ingrese su nombre.")}))
    cedula = forms.CharField(label="", max_length=13, widget=forms.TextInput(attrs={"placeholder": _("Cédula"), "title": _("Ingrese su número de cédula")}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder": _("Correo electrónico"), "title": _("Ingrese su correo electrónico")}))
    telefono = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": _("Teléfono"), "title": _("Ingrese su número de teléfono")}))
    nota = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": _("Escriba un breve comentario...")}))
    consentimiento = forms.BooleanField(label=_("Estoy de acuerdo con la política de privacidad"), widget=forms.CheckboxInput(attrs={"title": _("Indica que estás de acuerdo en enviarnos tus datos para ser evaluado.")}))


    def clean(self):
        """Operación de limpieza para validar los datos antes de guardar.
        """
        # Validamos la cédula ingresada.
        try:
            self.cleaned_data["cedula"] = self.ValidarCedula(self.cleaned_data["cedula"])
        except BaseException as e:
            raise ValidationError({"cedula": _("¡Ups! Al parecer la cédula no es válida. {}".format(e))})
        # Limpiamos el nombre para que sea en mayuscula.
        self.cleaned_data["nombre"] = self.cleaned_data["nombre"].upper()



