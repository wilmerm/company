"""
Módulo para la declaración de las variables globales 
comunes para todo el  proyecto.
"""

from django.utils.translation import gettext as _
from fuente.var import * # También se importa el diccionario 'VAR'.






# Espacio de configuración para la empresa -----------------------------------------------
# ----------------------------------------------------------------------------------------
PROJECT_NAME = "Company"
PROJECT_AUTHOR = "Wilmer Martínez"
PROJECT_AUTHOR_COMPANY = "PM Soluciones"
PROJECT_AUTHOR_URL = "http://www.wilmermartinez.com"
PROJECT_AUTHOR_EMAIL = "wilmermorelmartinez@gmail.com"
PROJECT_AUTHOR_PHONE = "+1-829-925-9531"
PROJECT_DESCRIPTION = _("")
# Sobre la empresa
COMPANY_NAME = "Soluciones Morel"
COMPANY_NAME2 = "Soluciones Morel SRL"
COMAPANY_IDENTIFICATION = ""
COMPANY_DESCRIPTION = _("Viviendas, Alquileres, Solares, Fincas, Préstamos")
COMPANY_EMAIL = "solusionesmorel@hotmail.com"
COMPANY_PHONE = "809-598-6155"
# Sobre la web
WEB_NAME = COMPANY_NAME
WEB_URL = "http://www.solucionesmorel.com"
# Título y descripción que se mostrará en las páginas, a menos que se 
# remplace su valor en el context de las views.
TITLE = WEB_NAME
DESCRIPTION = "{} {}. {}".format(_("Sitio web de "), COMPANY_NAME, COMPANY_DESCRIPTION)
# Redes sociales
URL_FACEBOOK = "https://www.facebook.com/SOLUCIONES-MOREL-265648666943445/"
URL_TWITTER = ""
URL_INSTAGRAM = ""
URL_LINKEDIN = ""


# Propiedades para SEO
FACEBOOK_APP_ID = "1884552708497884"
# --------------------------------------------------------------------------------------
# Fin de espacio de configuración para la empresa. -------------------------------------













# Agrege las aplicaciones instaladas (solo las nuestras) ----------------------------------
APLICATIONS = (
    ("clientes", _("Clientes")),
    ("contabilidad", _("Contabilidad")),
    ("prestamos", _("Préstamos")),
    ("tienda", _("Tienda")),
    ("blog", _("Blog")),
)







# Imagenes que se encuentran en la carpeta static del proyecto.
# Imagenes principales:
IMG_LOGO = STATIC_URL + "base/img/logo1.svg"
IMG_LOGO_ICON = STATIC_URL + "base/img/logo_icon.png" # imágen que se muestra en la pestaña del navegador.
IMG_DEFAULT = IMG_LOGO
IMG_HOME = IMG_DEFAULT
# Imagenes genéricas:
IMG_GOOD = STATIC_URL + "base/img/good.png"
IMG_MENU = STATIC_URL + "base/img/menu.svg"
IMG_FORM = STATIC_URL + "base/img/form.png"
# Redes sociales:
IMG_GPLUS = STATIC_URL + "base/img/social/gplus.svg"
IMG_FACEBOOK = STATIC_URL + "base/img/social/facebook.svg"
IMG_INSTAGRAM = STATIC_URL + "base/img/social/instagram.svg"
IMG_LINKEDIN = STATIC_URL + "base/img/social/linkedin.svg"
IMG_PINTEREST = STATIC_URL + "base/img/social/pinterest.svg"
IMG_TWITTER = STATIC_URL + "base/img/social/twitter.svg"
IMG_VK = STATIC_URL + "base/img/social/vk.svg"
# Imágenes de la aplicación 'prestamos':
IMG_PRESTAMOS = STATIC_URL + "prestamos/img/prestamos.png"
IMG_PRESTAMOS_CALCULADORA = STATIC_URL + "prestamos/img/calculadora.png"
IMG_PRESTAMOS_DINERO = STATIC_URL + "prestamos/img/dinero.png"
IMG_PRESTAMOS_SOLICITUD = STATIC_URL + "prestamos/img/solicitud.png"
# Imágenes de la aplicación 'tienda':
IMG_TIENDA = STATIC_URL + "tienda/img/tienda.png"
IMG_TIENDA_POST = STATIC_URL + "tienda/img/articulo.png"
# Imágenes de la aplicación 'blog':
IMG_BLOG = STATIC_URL + "blog/img/blog.png"
IMG_BLOG_ARTICLE = "blog/img/article.png"



# Enlaces y listado de enlaces.  ----------------------------------------------------------
# Estos son los grupos de enlaces, cada enlace que se declare, pertenecerá a uno de
# estos grupos.
NAV = "NAV"
CREDITS = "CREDITS"
SOCIAL = "SOCIAL"
LINK_CHOICES = (
    (NAV, _("Barra de navegación")),
    (CREDITS, _("Créditos")),
    (SOCIAL, _("Redes sociales")),
)
# También hay enlaces que pertenecen a aplicaciones especificas, por eso sumamos a la
# lista de enlaces, las aplicaciones instaladas.
LINK_CHOICES = tuple(list(LINK_CHOICES) + list(APLICATIONS))








# Actualizamos las variables globales, con las variables de esta aplicación.
# Nota 1: Las variables globales son las que se encuentran en el módulo 'fuente' el cual contiene otros módulos.
# Nota 2: Esto debe ir siempre al final, luego de declarar todas las variables para que
# las pueda tomar todas.
VAR.update(vars().copy())









