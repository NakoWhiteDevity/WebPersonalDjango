from django.db import models

# Create your models here.
class Experiencia(models.Model):
    puesto = models.CharField(verbose_name = "Puesto de trabajo", max_length=50)
    ano = models.IntegerField(verbose_name = "Año")
    duracion = models.CharField(verbose_name = "Duración",max_length=20)
    lugar = models.CharField(verbose_name= "Lugar", max_length=50)
    tareas = models.TextField(verbose_name = "Descripción y tareas", max_length=600)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "experiencia"
        verbose_name_plural = "experiencias"
        ordering = ["-creado"]

    def __str__(self):
        return "{0} en {1}".format(self.puesto, self.lugar)

class Formacion(models.Model):
    formacion = models.CharField(verbose_name = "Formación recibida", max_length=50)
    ano = models.CharField(verbose_name = "año/s de realización", max_length=10)
    lugar = models.CharField (verbose_name= "Lugar de realización", max_length=50)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "formacion"
        verbose_name_plural = "formaciones"
        ordering = ["-creado"]
    
    def __str__(self):
        return "{0} en {1} [{2}]".format(self.formacion, self.lugar, self.ano)

class DatosDeInteres(models.Model):
    dato = models.CharField(verbose_name = "Dato de interes", max_length=50)

    class Meta:
        verbose_name = "dato de interes"
        verbose_name_plural = "datos de interes"
        ordering = ["dato"]

    def __str__(self):
        return self.dato
