from django.db import models

class Procesador(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=50)
    año_lanzamiento = models.PositiveIntegerField()
    frecuencia_base = models.FloatField(help_text="Frecuencia base en GHz")
    frecuencia_maxima = models.FloatField(help_text="Frecuencia máxima en GHz")
    numero_nucleos = models.PositiveIntegerField()
    numero_hilos = models.PositiveIntegerField()
    cache_L3 = models.FloatField(help_text="Tamaño de la caché L3 en MB")
    tdp = models.FloatField(help_text="TDP en vatios")
    arquitectura = models.CharField(max_length=50)
    tecnologia_fabricacion = models.FloatField(help_text="Tecnología de fabricación en nm")
    soporte_multithreading = models.BooleanField(default=False)
    precio_lanzamiento = models.FloatField(help_text="Precio de lanzamiento en USD")

    def __str__(self):
        return f"{self.nombre} ({self.fabricante})"

    class Meta:
        verbose_name = "Procesador"
        verbose_name_plural = "Procesadores"
        ordering = ['año_lanzamiento']
