
import datetime
from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import gettext as _

from fuente.base import Texto, Numero, Fecha
from .models import *




