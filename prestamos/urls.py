"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='prestamos'),
    path('solicitud/', views.SolicitudView.as_view(), name='prestamos_solicitud'),
    path('solicitud/enviada/', views.SolicitudEnviadaView.as_view(), name='prestamos_solicitud_enviada'),
    path('calculadora/', views.CalculadoraView.as_view(), name='prestamos_calculadora'),
    path('prestamo/create/', views.PrestamoCreateView.as_view(), name='prestamos_prestamo_create'),
]
