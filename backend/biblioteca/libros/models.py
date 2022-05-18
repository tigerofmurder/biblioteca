# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

def uploadPortada(instance, filename):
    return "{}-{}".format(
        instance.id,
        filename
    )

class libros(models.Model):
    titulo = models.CharField(
        max_length=250
    )
    autor = models.CharField(
        max_length=250
    )
    anhoPublicacion = models.IntegerField(
        blank = False,
        null=True
    )
    edicion = models.IntegerField(
        blank = False,
        null=True
    )
    imagenPortada = models.ImageField(
        upload_to=uploadPortada,
        blank=False,
        null=True
    )
    cantidadEjemplares = models.PositiveIntegerField(
        default=0
    )
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return "{}-{}".format(
        self.pk,
        self.filename
    )