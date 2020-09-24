from django.contrib import admin
from .models import Enlace

#Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('clave','nombre',)
    list_display = ('nombre',)

admin.site.register(Enlace,EnlaceAdmin)