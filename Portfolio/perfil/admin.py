from django.contrib import admin
from .models import Experiencia, Formacion, DatosDeInteres

# Register your models here.
class ExperienciaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('puesto','lugar','ano')

admin.site.register(Experiencia, ExperienciaAdmin)

class FormacionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('formacion','lugar','ano')

admin.site.register(Formacion, FormacionAdmin)

class DatosDeInteresAdmin(admin.ModelAdmin):
    pass

admin.site.register(DatosDeInteres, DatosDeInteresAdmin)
