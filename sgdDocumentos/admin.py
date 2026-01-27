from django.contrib import admin

# Register your models here.
from .models import (
    DocumentType,
    Document,
    DocumentVersion,
    DocumentMetadata
)


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class DocumentMetadataInline(admin.TabularInline):
    model = DocumentMetadata
    extra = 1


class DocumentVersionInline(admin.TabularInline):
    model = DocumentVersion
    extra = 0
    readonly_fields = ("created_at",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "document_type",
        "created_by",
        "created_at",
        "is_active",
    )
    list_filter = ("document_type", "is_active", "created_at")
    search_fields = ("title", "description")
    readonly_fields = ("created_at",)

    inlines = [
        DocumentMetadataInline,
        DocumentVersionInline,
    ]
