"""
Modelo de apps DB
"""

from django.db import models



class Departamento(models.Model):
    nombre = models.CharField('Nombre del departamento', max_length=50)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self) -> str:
        return f"{self.id} - {self.nombre} - {self.created} - {self.updated}"


class Alcalde(models.Model):
    nombre_alcalde = models.CharField('Nombre del alcalde', max_length=50, unique=True)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)


class Municipio(models.Model):
    nombre = models.CharField('Nombre del municipio', max_length=50)
    alcalde = models.ForeignKey(Alcalde, on_delete=models.CASCADE)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

