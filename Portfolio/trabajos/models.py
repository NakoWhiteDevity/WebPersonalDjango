from django.db import models

# Create your models here.
class Trabajo(models.Model):
    nombre = models.CharField(verbose_name = "Nombre del proyecto", max_length=50)
    autor = models.CharField(verbose_name = "Autor/es o empresa creadora", max_length=50)
    foto = models.ImageField(verbose_name = "Foto del proyecto", upload_to="Trabajos")
    enlace = models.URLField(verbose_name = "Enlace del proyecto", null=True, blank=True)
    descripcion = models.TextField(verbose_name = "Descripción del proyecto", max_length=600, null=True)
    fechafin = models.DateField(verbose_name = "Fecha de fin de proyecto", null=True, blank=True)

    class Meta:
        verbose_name = "trabajo"
        verbose_name_plural = "trabajos"

    def __str__(self):
        return self.nombre
