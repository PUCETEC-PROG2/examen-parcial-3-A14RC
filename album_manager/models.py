from django.db import models
from django.urls import reverse



class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Descripción no disponible")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('artista-detail', kwargs={'pk': self.pk})


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    anio_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portadas/')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('album-detail', kwargs={'pk': self.pk})