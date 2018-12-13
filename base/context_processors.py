from django.contrib.auth.models import User




from fuente import base, email, encriptado, paises, mobile
from .var import *
from .links import links
from .models import *



CONTEXT = {}
CONTEXT.update(VAR)
CONTEXT["links"] = links
CONTEXT["conf"] = Configuration()
CONTEXT["IMAGE"] = IMG_LOGO





def context(request):
    return CONTEXT