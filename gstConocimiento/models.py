from django.db import models

class sgdDocumento(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    publication_date = models.DateField()
    issn = models.CharField(max_length=50, blank=True)

    file = models.FileField(upload_to="sgdDocumentos/")

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
