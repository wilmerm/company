from django.utils.translation import gettext_lazy as _
# Locales
from .paises import *


try:
    from django.conf import settings
    STATIC_URL = settings.STATIC_URL
except BaseException:
    STATIC_URL = ""






# Espacio de configuración para la empresa -----------------------------------------------
# ----------------------------------------------------------------------------------------
PROJECT_NAME = "Company"
PROJECT_AUTHOR = "Wilmer Martínez"
PROJECT_AUTHOR_URL = "http://www.wilmermartinez.com"
PROJECT_AUTHOR_EMAIL = "wilmermorelmartinez@gmail.com"
PROJECT_AUTHOR_PHONE = "+1-829-925-9531"
PROJECT_DESCRIPTION = _("")
# Sobre la empresa
COMPANY_NAME = "Peña & Martínez"
COMPANY_NAME2 = "Peña & Martínez SRL"
COMPANY_DESCRIPTION = _("Somos una empresa dedicada a ofrecer servicios inmobiliarios, préstamos personales, diseño web empresarial, servicios jurídicos en general...")
# Sobre la web
WEB_NAME = "Peña & Martínez"
WEB_URL = ""
# Título y descripción que se mostrará en las páginas, a menos que se 
# remplace su valor en el context de las views.
TITLE = "Peña & Martínez"
DESCRIPTION = "{} {}. {}".format(_("Sitio web de "), COMPANY_NAME, COMPANY_DESCRIPTION)
# Redes sociales
URL_FACEBOOK = "https://www.facebook.com/wilmermartinez01"
URL_TWITTER = "https://twitter.com/wilmermorel"
URL_INSTAGRAM = "https://www.instagram.com/wilmermartinez.1/"
URL_LINKEDIN = "https://www.linkedin.com/in/wilmerm/"


# Propiedades para SEO
FACEBOOK_APP_ID = "1884552708497884"
# --------------------------------------------------------------------------------------
# Fin de espacio de configuración para la empresa. -------------------------------------









# PERSONAS -----------------------------------------------------------

MASCULINO = "M"
FEMENINO = "F"
NO_DEFINIDO = "ND"
SEXO_CHOICES = (
    (MASCULINO, _("Masculino")),
    (FEMENINO, _("Femenino")),
    (NO_DEFINIDO, _("No definido")),
)



# CONTABILIDAD -------------------------------------------------------

DOP = "DOP"
USD = "USD"
EUR = "EUR"
CAD = "CAD"
GSB = "GSB"
MONEDA_CHOICES = (
    (DOP, _("DOP: Peso dominicano")),
    (USD, _("USD: Dólar estadounidense")),
    (EUR, _("EUR: Euro")),
    (CAD, _("CAD: Dólar canadiense")),
    (GSB, _("GSB: Libra esterlina")),
)

EFECTIVO = "EF"
CUENTA_CORRIENTE = "CC"
CUENTA_AHORROS = "CA"
PRESTAMO = "PR"
TARJETA_CREDITO = "TC"
TARJETA_DEBITO = "TD"
CUENTA_CHOICES = (
    (EFECTIVO, _("Efectivo")),
    (CUENTA_CORRIENTE, _("Cuenta corriente")),
    (CUENTA_AHORROS, _("Cuenta de ahorros")),
    (PRESTAMO, _("Préstamo")),
    (TARJETA_CREDITO, _("Tarjeta de crédito")),
    (TARJETA_DEBITO, _("Tarjeta de débito")),
)

CUOTA_FIJA = "FIJA"
CUOTA_VARIABLE = "VARIABLE"
CUOTA_TIPOS = (
    (CUOTA_FIJA, _("Cuota fija")),
    (CUOTA_VARIABLE, _("Cuota variable")),
)




# FECHAS ------------------------------------------------------------

DIARIO = "DIARIO"
SEMANAL = "SEMANAL"
QUINCENAL = "QUINCENAL"
MENSUAL = "MENSUAL"
ANUAL = "ANUAL"
PERIODO_CHOICES = (
    (DIARIO, _("Diario")),
    (SEMANAL, _("Semanal")),
    (QUINCENAL, _("Quincenal")),
    (MENSUAL, _("Mensual")),
    (ANUAL, _("Anual")),
)




# INFORMÁTICA ------------------------------------------------------

TUPLE = "TUPLE"
LIST = "LIST"
DICT = "DICT"
INT = "INT"
FLOAT = "FLOAT"
DECIMAL = "DECIMAL"
STR = "STR"
BOOL = "BOOL"
TIPO_DE_DATOS_CHOICES = (
    (STR, "Texto"),
    (INT, "Número entero."),
    (FLOAT, "Número de coma flotante."),
    (DECIMAL, "Número decimal"),
    (TUPLE, "Tupla"),
    (LIST, "Lista"),
    (DICT, "Diccionario"),
    (BOOL, "Falso/Verdadero")
)






# IMÁGENES. ----------------------------------------------------------

IMG_DINERO = STATIC_URL + "img/dinero.svg"




















# Todas las variables (esto debe ir siempre al final del archivo, 
# para que tome todas las variables)
VAR = vars().copy()
