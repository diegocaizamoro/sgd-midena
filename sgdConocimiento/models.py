from django.db import models
from django.utils import timezone
from sgdCatalogo.models import RedesInvestigacion, AplicacionPotencial, Referencia


class SgdConocimiento(models.Model):

    codigo = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    titulo = models.CharField(max_length=255)

    resumen = models.TextField(
        blank=True,
        null=True
    )

    red_investigacion = models.ForeignKey(
        RedesInvestigacion,
        on_delete=models.PROTECT,
        related_name="conocimientos"
    )

    aplicacion_potencial = models.ForeignKey(
        AplicacionPotencial,
        on_delete=models.PROTECT,
        related_name="conocimientos"
    )

    referencia = models.ForeignKey(
        Referencia,
        on_delete=models.PROTECT,
        related_name="conocimientos"
    )

    archivo = models.FileField(
        upload_to="sgdConocimiento/"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Conocimiento"
        verbose_name_plural = "Gestión de Conocimiento"
        ordering = ["-fecha_creacion"]

    def save(self, *args, **kwargs):
        if not self.codigo:
            ultimo = SgdConocimiento.objects.order_by("-id").first()
            if ultimo:
                numero = ultimo.id + 1
            else:
                numero = 1
            self.codigo = f"GC-{numero:05d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"