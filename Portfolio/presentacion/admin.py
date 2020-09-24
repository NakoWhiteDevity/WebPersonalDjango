from django.contrib import admin
from .models import Foto, Texto

# Register your models here.

class FotoAdmin(admin.ModelAdmin):
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="personal").exists():
            return ('clave',)
        else:
            return ()

admin.site.register(Foto,FotoAdmin)

class TextoAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="personal").exists():
            return ('clave',)
        else:
            return ()

admin.site.register(Texto,TextoAdmin)