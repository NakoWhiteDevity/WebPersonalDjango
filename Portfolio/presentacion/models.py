from django.db import models

# Create your models here.
class Foto(models.Model):
    clave = models.CharField(verbose_name="clave", max_length=20)
    foto = models.ImageField(verbose_name = "foto", upload_to="FotoPresentacion")

    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "foto"
    
    def __str__(self):
        return "Foto de presentación."

class Texto(models.Model):
    clave = models.CharField(verbose_name="clave", max_length=20)
    texto = models.TextField(verbose_name="Presentación", max_length=700)

    class Meta:
        verbose_name = "texto"
        verbose_name_plural = "texto"
    
    def __str__(self):
        return "texto de presentación"

