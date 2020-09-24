#Permite añadir el nombre en castellano de la app en el administrador de Django.

from django.apps import AppConfig


class NombreyredesConfig(AppConfig):
    name = 'nombreyredes'
    verbose_name = 'nombre, rol y redes'
