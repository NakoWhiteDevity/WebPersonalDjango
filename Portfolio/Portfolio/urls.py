"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core import views as core_views
from perfil import views as perfil_views
from trabajos import views as trabajos_views

from django.conf import settings

urlpatterns = [
    #path del admin
    path('admin/', admin.site.urls),
    #path de la web
    path('',core_views.sobremi, name="sobremi"),
    path('perfil/',perfil_views.perfil, name="perfil"),
    path('trabajos/',trabajos_views.trabajos, name="trabajos"),
]

#Comentamos esta linea de cara a producción
"""
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""