from django.contrib import admin
from .models import Trabajo

# Register your models here.
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('nombre','autor','fechafin')

admin.site.register(Trabajo, TrabajoAdmin)
