from django.shortcuts import render
from .models import Experiencia, Formacion, DatosDeInteres

# Create your views here.
def perfil(request):
    experiencias = Experiencia.objects.all()
    formaciones = Formacion.objects.all()
    datos = DatosDeInteres.objects.all()
    return render(request, "perfil/perfil.html",{'experiencias':experiencias,'formaciones':formaciones,'datos':datos})
