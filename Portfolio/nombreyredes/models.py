from django.db import models

# Create your models here.

class Enlace(models.Model):
    clave = models.SlugField(max_length=20, unique=True, verbose_name="Clave")
    nombre = models.CharField(max_length=20, verbose_name="Red social")
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="Enlace")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name_plural = "redes sociales"
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre

