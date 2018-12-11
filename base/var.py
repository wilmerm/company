"""
Módulo para la declaración de las variables globales 
comunes para todo el  proyecto.
"""

from django.utils.translation import gettext as _
from fuente.var import * # También se importa el diccionario 'VAR'.




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
IMG_LOGO = STATIC_URL + "base/img/logo1.png"
IMG_DEFAULT = IMG_LOGO
IMG_HOME = IMG_DEFAULT
# Imagenes genéricas:
IMG_GOOD = STATIC_URL + "base/img/good.png"
IMG_MENU = STATIC_URL + "base/img/menu.svg"
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









