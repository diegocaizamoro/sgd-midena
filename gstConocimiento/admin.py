from django.contrib import admin

# Register your models here.
from .models import sgdDocumento


@admin.register(sgdDocumento)
class RevistaAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "publication_date",
        "issn",
    )
    search_fields = ("title", "issn")
    list_filter = ("publication_date",)

