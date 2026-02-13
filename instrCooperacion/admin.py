from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import InstrumentoCooperacion


@admin.register(InstrumentoCooperacion)
class InstrumentoCooperacionAdmin(ModelAdmin):

    # Columnas visibles en la lista principal
    list_display = (
        "codigo",
        "ambito_de_cooperacion",
        "objeto",
        "fecha_suscripcion",
        "fecha_creacion",
    )

    # Campos por los que se puede buscar
    search_fields = (
        "codigo",
        "objeto",
        "alcance",
        "productos_entregables",
    )

    # Filtros laterales
    list_filter = (
        "ambito_de_cooperacion",
        "fecha_suscripcion",
        "fecha_creacion",
    )

    # Campos de solo lectura (importante para el código autogenerado)
    readonly_fields = (
        "codigo",
        "fecha_creacion",
        "fecha_actualizacion",
    )

    # Orden predeterminado (más reciente primero)
    ordering = ("-fecha_creacion",)

    # Organización del formulario de edición por secciones (Estilo Unfold)
    fieldsets = (
        ("Información General", {
            "fields": (
                "codigo",
                "ambito_de_cooperacion",
                "fecha_suscripcion",
            )
        }),
        ("Definición Técnica", {
            "fields": (
                "objeto",
                "alcance",
                "impacto_institucional",
            )
        }),
        ("Entregables y Compromisos", {
            "fields": (
                "productos_entregables",
                "compromisos_de_las_partes",
                "logros_alcanzados",
            )
        }),
        ("Soporte Documental", {
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