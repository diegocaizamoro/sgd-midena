from django.contrib import admin
from unfold.admin import ModelAdmin
from sgdCatalogo.models import KnowledgeDocumentType

# Register your models here.
@admin.register(KnowledgeDocumentType)
class KnowledgeDocumentTypeAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name',)   # 👈 ESTO HABILITA LA EDICIÓN
    actions = ["delete_selected"]