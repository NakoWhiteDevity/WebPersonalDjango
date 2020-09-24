#En este fichero se generan las funciones que generan a su vez los diccionarios de contexto globales a la web.
#Para añadir el diccionario de contexto global hay que añadirlo en la lista de settings de context_processors bajo la sintaxis: app.(fichero py con el diccionario)."funcion que genera el diccionario".

from .models import Foto, Texto

def contextopresentacion(request):
    dicpresentacion = {}
    fotos = Foto.objects.all()
    for foto in fotos:
        dicpresentacion[foto.clave] = foto.foto
    textos = Texto.objects.all()
    for texto in textos:
        dicpresentacion[texto.clave] = texto.texto
    return dicpresentacion