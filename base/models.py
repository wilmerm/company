# Python
import os
import datetime

# Django.
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _

# Locales:
from fuente import base, email, encriptado, paises
from .var import *





class Configuration(models.Model):
    """
    Registra las configuraciones global del proyecto.
    """
    name = models.CharField(_("Nombre"), max_length=50)
    value = models.TextField(_("Valor"))
    value_type = models.CharField(_("Tipo"), max_length=50, choices=TIPO_DE_DATOS_CHOICES, default=STR)

    class Meta:
        verbose_name = _("Configuración")
        verbose_name_plural = _("Configuraciones")

    def __str__(self):
        return self.name

    def __iter__(self):
        for conf in self.GetAll():
            yield conf

    def __getitem__(self, name):
        return self.Get(name)

    def get_absolute_url(self):
        return reverse("Configurations_detail", kwargs={"pk": self.pk})

    def Convert(self, type=None):
        """Convierte el valor de esta instancia al tipo de valor indicado.
        Si no se especifica ningún valor, se toma el valor de la variable value_type.
        """
        if type == None:
            type = self.value_type
        if type == STR:
            return str(self.value)
        elif type == INT:
            return int(self.value)
        elif type == FLOAT: 
            return float(self.value)
        elif type == LIST:
            return list(self.value)
        elif type == TUPLE:
            return tuple(self.value)
        elif type == DICT:
            return dict(self.value)
        elif type == BOOL:
            if self.value.lower() in ("false", "0", "no"):
                return False
            if self.value.lower() in ("true", "1", "yes", "si"):
                return True
            else:
                return bool(self.value)
        return self.value

    def Get(self, name):
        """Obtiene la configuración con el nombre indicado.
        Si no existe dicha configuración registrada en la base datos, 
        entonces la busca en las variables globales del modulo fuente.
        """
        conf = Configuration.objects.get(name, "--NULL--")
        if conf == "--NULL--":
            try:
                conf = VAR[name]
            except KeyError:
                raise KeyError(_("La configuración o variable '{}' no existe.".format(name)))
        else:
            conf = conf.Convert()
        return conf

    def GetAll(self):
        return Configuration.objects.all()

    def GetDict(self):
        """Obtiene un diccionario con los nombres de las configuraciones con keys, y los 
        valores ya convertidos a su tipo indicado.
        """
        dic = {}
        for conf in self.GetAll():
            dic[conf.name] = conf.GetValue()
        return dic

    def GetValue(self, type=None):
        """Obtiene el valor ya convertido a su tipo.
        """
        return self.Convert(type)
    













    

    




