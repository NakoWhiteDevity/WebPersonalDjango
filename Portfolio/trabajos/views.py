from django.shortcuts import render
from .models import Trabajo

# Create your views here.
def trabajos(request):
    trabajos = Trabajo.objects.all()
    return render(request, "trabajos/trabajos.html", {'trabajos':trabajos})
