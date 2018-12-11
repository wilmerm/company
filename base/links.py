"""
Módulo para la declaración de los distintos enlaces que 
se usarán en todo el proyecto.
"""

from django.utils.translation import gettext as _
from django.urls import reverse, reverse_lazy
from .var import * # También se importa el diccionario 'VAR'.



# Enlaces y listado de enlaces.  ----------------------------------------------------------
# Estos son los grupos de enlaces, cada enlace que se declare, pertenecerá a uno de
# estos grupos.
NAV = "NAV" # Barra de navegación.
CREDITS = "CREDITS" # Listado de créditos y otros enlaces en el footer.
SOCIAL = "SOCIAL" # Listado de enlaces para redes sociales.
PRESTAMOS = "PRESTAMOS" # Aplicación 'prestamos'.
TIENDA = "TIENDA" # Aplicación 'tienda'.
BLOG = "BLOG" # Aplicación blog.


class Link():
    """
    Crea un link que se usará en el proyecto.
    """
    def __init__(self, id, name, group=NAV, view=None, url="", cssclass="link", img=IMG_DEFAULT, description="", target=""):
        """
        Args:
            id: un identificador único en formato string.
            name: nombre del enlace.
            group: grupo del enlaces al cual pertenece.
            view: nombre de la vista.
            url: dirección url a la que apunta (opcional, solo se usará si view es None).
            cssclass: clase de estilo CSS para aplicar en las plantillas.
            img: es la ruta de la imagen en la carpeta 'static'.
            desc: breve descripción que se mostrará en el enlace.
            target: es la opción para los enlaces HTML que indican si se abre otra pestaña '_blank' o no ''.
        """
        self.id = id
        self.name = name
        self.group = group
        self.view = view 
        self.url = url 
        self.cssclass = cssclass 
        self.img = img
        self.description = description
        self.target = target

    def __str__(self):
        return self.name

    def Url(self):
        if not self.view:
            return self.url 
        return reverse(self.view)

    def GetImg(self):
        return self.img






class Links(dict):
    """Diccionario que almacena todos los enlaces declarados.
    Este es el objeto que se pasará a las plantillas.
    """

    def Add(self, *args):
        """Agrega uno o varios enlaces
        """
        for arg in args:
            self[arg.id] = arg
    
    def GetGroups(self):
        """Obtiene un diccionario con los grupos de enlaces como claves,
        y un listado de objetos Link como valores para cada clave.
        """
        out = dict()
        for key in self:
            value = self[key]
            if value.group in out:
                out[value.group].append(value)
            else:
                out[value.group] = [value]
        return out

    def GetCredits(self):
        """Obtiene el listado de enlaces que conforman el grupo de 
        los créditos y otros enlaces de referencias.
        """
        out = []
        for key in self:
            value = self[key]
            if value.group == CREDITS:
                out.append(value)
        return out

    def GetNav(self):
        """Obtiene el listado de enlaces que conforman el grupo de
        la barra de navegación.
        """
        out = []
        for key in self:
            value = self[key]
            if value.group == NAV:
                out.append(value)
        return out


    def GetSocial(self):
        """Obtiene el listado de enlaces que conforman el grupo de 
        las redes sociales de la empresa.
        Puede configurar la url a la que apuntan en el módulo fuente/var.py
        """
        out = []
        for key in self:
            value = self[key]
            if value.group == SOCIAL:
                out.append(value)
        return out





# Declaramos los enlaces: ------------------------------------------------------------------

# Barra de navegación:
index = Link(id="index", name=_("Inicio"), view="index", img=IMG_HOME, description=_("Página principal."))
prestamos = Link(id="prestamos", name=_("Préstamos"), view="prestamos", img=IMG_PRESTAMOS, description=_("Gestión de préstamos."))
tienda = Link(id="tienda", name=_("Tienda"), view="tienda", img=IMG_TIENDA, description=_("Tienda en línea."))
blog = Link(id="blog", name=_("Blog"), view="blog", img=IMG_BLOG, description=_("Nuevas publicaciones en el blog."))

# Créditos:
author = Link(id="author", name="{} {}".format(_("Desarrollado por"), PROJECT_AUTHOR_COMPANY), group=CREDITS, url=PROJECT_AUTHOR_URL, description=_("Creación: {} | {}".format(PROJECT_AUTHOR, PROJECT_AUTHOR_EMAIL)), target="_blank")
author_email = Link(id="author_email", name="{}".format(PROJECT_AUTHOR_PHONE), group=CREDITS, description=_("Creación: {} | {}".format(PROJECT_AUTHOR, PROJECT_AUTHOR_EMAIL)), target="_blank")
politica_de_privacidad = Link(id="politica_de_privacidad", name=_("Política de privacidad"), group=CREDITS, view="politica_de_privacidad", description=_("Vea nuestra política de privacidad"), target="_blank")

# Social
facebook = Link(id="facebook", name="Facebook", group=SOCIAL, url=URL_FACEBOOK, img=IMG_FACEBOOK, target="_blank", description="Facebook")
twitter = Link(id="twitter", name="Twitter", group=SOCIAL, url=URL_TWITTER, img=IMG_TWITTER, target="_blank", description="Facebook")
instagram = Link(id="instagram", name="Instagram", group=SOCIAL, url=URL_INSTAGRAM, img=IMG_INSTAGRAM, target="_blank", description="Instagram")
linkedin = Link(id="linkedin", name="LinkeIn", group=SOCIAL, url=URL_LINKEDIN, img=IMG_LINKEDIN, target="_blank", description="LinkedIn")

# App 'prestamos':
prestamos_solicitud = Link(id="prestamos_solicitud", name=_("Solicitar préstamo"), group="prestamos", view="prestamos_solicitud", img=IMG_PRESTAMOS_SOLICITUD, description=_("¡Solicite su préstamo personal ahora mismo!"))
prestamos_calculadora = Link(id="prestamos_calculadora", name=_("Calculadora de préstamo"), group="prestamos", view="prestamos_calculadora", img=IMG_PRESTAMOS_CALCULADORA, description=_("Utilice la herramienta para calcular las cuotas de su préstamo."))

# App 'tienda':
tienda_post = Link(id="tienda_post", name=_("Publicaciones"), group="tienda", view="tienda_post_list", img=IMG_TIENDA_POST, description=_("Vea los nuevos artículos publicados."))

# App 'blog':



# Añadimos los enlaces al diccionario:
links = Links()
links.Add(
    # barra de navegación
    index, 
    prestamos, 
    tienda, 
    blog,
    # creditos
    author, 
    author_email, 
    # social
    facebook,
    twitter,
    instagram,
    linkedin,
    # App prestamos
    politica_de_privacidad, 
    prestamos_solicitud, 
    prestamos_calculadora,
    # App tienda
    tienda_post,
    )






