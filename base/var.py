"""
Módulo para la declaración de las variables globales 
comunes para todo el  proyecto.
"""

from django.utils.translation import gettext as _
from fuente.var import * # También se importa el diccionario 'VAR'.




# Agrege las aplicaciones instaladas (solo las nuestras) ----------------------------------
APLICATIONS = (
    ("prestamos", _("Préstamos")),
)









# Imagenes que se encuentran en la carpeta static del proyecto.
# Imagenes principales:
IMG_LOGO = STATIC_URL + "base/img/logo1.png"
IMG_DEFAULT = IMG_LOGO
IMG_HOME = IMG_DEFAULT
# Imagenes genéricas:
IMG_GOOD = STATIC_URL + "base/img/good.png"
# Imagenes de la aplicación 'prestamos':
IMG_PRESTAMOS = STATIC_URL + "prestamos/img/prestamos.png"
IMG_PRESTAMOS_CALCULADORA = STATIC_URL + "prestamos/img/calculadora.png"
IMG_PRESTAMOS_DINERO = STATIC_URL + "prestamos/img/dinero.png"
IMG_PRESTAMOS_SOLICITUD = STATIC_URL + "prestamos/img/solicitud.png"







# Enlaces y listado de enlaces.  ----------------------------------------------------------
# Estos son los grupos de enlaces, cada enlace que se declare, pertenecerá a uno de
# estos grupos.
NAV = "NAV"
CREDITS = "CREDITS"
LINK_CHOICES = (
    (NAV, _("Barra de navegación")),
    (CREDITS, _("Créditos")),
)
# También hay enlaces que pertenecen a aplicaciones especificas, por eso sumamos a la
# lista de enlaces, las aplicaciones instaladas.
LINK_CHOICES = tuple(list(LINK_CHOICES) + list(APLICATIONS))








# Actualizamos las variables globales, con las variables de esta aplicación.
# Nota 1: Las variables globales son las que se encuentran en el módulo 'fuente' el cual contiene otros módulos.
# Nota 2: Esto debe ir siempre al final, luego de declarar todas las variables para que
# las pueda tomar todas.
VAR.update(vars().copy())









