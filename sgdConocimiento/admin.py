from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SgdConocimiento

@admin.register(SgdConocimiento)
class SgdConocimientoAdmin(ModelAdmin):

    list_display = (
        "codigo",
        "titulo",
        "red_investigacion",
        "aplicacion_potencial",
        "referencia",
        "fecha_creacion",
    )

    search_fields = (
        "codigo",
        "titulo",
        "resumen",
    )

    list_filter = (
        "red_investigacion",
        "aplicacion_potencial",
        "referencia",
        "fecha_creacion",
    )

    readonly_fields = (
        "codigo",
        "fecha_creacion",
        "fecha_actualizacion",
    )

    ordering = ("-fecha_creacion",)

    fieldsets = (
        ("Información General", {
            "fields": (
                "codigo",
                "titulo",
                "resumen",
            )
        }),
        ("Clasificación", {
            "fields": (
                "red_investigacion",
                "aplicacion_potencial",
                "referencia",
            )
        }),
        ("Archivo", {
            "fields": (
                "archivo",
            )
        }),
        ("Fechas del Sistema", {
            "fields": (
                "fecha_creacion",
                "fecha_actualizacion",
            )
        }),
    )
