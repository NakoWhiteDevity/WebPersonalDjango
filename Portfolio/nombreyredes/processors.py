#En este fichero se generan las funciones que generan a su vez los diccionarios de contexto globales a la web.
#Para añadir el diccionario de contexto global hay que añadirlo en la lista de settings de context_processors bajo la sintaxis: app.(fichero py con el diccionario)."funcion que genera el diccionario".

from .models import Enlace

def contextoredes(request):
    dicredes = {}
    links = Enlace.objects.all()
    for link in links:
        dicredes[link.clave] = link.url
    return dicredes