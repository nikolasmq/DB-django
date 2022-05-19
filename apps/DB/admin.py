from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Departamento)
class DepartamentoModelAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'nombre'
    )

    list_display_links = (
        'id',
        'nombre'
    )

    search_fields = (
        'id',
        'nombre'
    )

    list_filter = (
        'id',
        'nombre'
    )

    readonly_fields = (
        'created',
        'updated'
    )


@admin.register(models.Alcalde)
class AlcaldeModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_alcalde'
    )

    list_display_links = (
        'id',
        'nombre_alcalde'
    )

    search_fields = (
        'id',
        'nombre_alcalde'
    )

    list_filter = (
        'id',
        'nombre_alcalde'
    )

    readonly_fields = (
        'created',
        'updated'
    )