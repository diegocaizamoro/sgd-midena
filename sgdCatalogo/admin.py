from django.contrib import admin
from unfold.admin import ModelAdmin
from sgdCatalogo.models import AplicacionPotencial, KnowledgeDocumentType, RedesInvestigacion, Referencia
# Register your models here.
@admin.register(KnowledgeDocumentType)
class KnowledgeDocumentTypeAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name',)   # 👈 ESTO HABILITA LA EDICIÓN
    actions = ["delete_selected"]

@admin.register(RedesInvestigacion)
class RedesInvestigacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    actions = ["delete_selected"]


@admin.register(AplicacionPotencial)
class AplicacionPotencialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    actions = ["delete_selected"]


@admin.register(Referencia)
class ReferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    actions = ["delete_selected"]