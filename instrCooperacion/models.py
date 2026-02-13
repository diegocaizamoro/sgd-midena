from django.db import models

class InstrumentoCooperacion(models.Model):
    AMBITO_CHOICES = [
        ('I+D+i', 'I+D+i'),
        ('estudio', 'Estudio'),
        ('transferencia', 'Transferencia del conocimiento'),
        ('intercambio', 'Intercambio de productos y servicios'),
        ('formacion', 'Formación'),
        ('comercializacion', 'Comercialización'),
        ('cofabricacion', 'Cofabricación'),
    ]

    # --- Identificación ---
    codigo = models.CharField(
        max_length=25,
        unique=True,
        editable=False,
        verbose_name="Código de Instrumento"
    )

    ambito_de_cooperacion = models.CharField(
        max_length=50,
        choices=AMBITO_CHOICES,
        verbose_name="Ámbito de Cooperación"
    )

    # --- Detalles Técnicos ---
    objeto = models.CharField(max_length=255, verbose_name="Objeto", null=True, blank=True)
    alcance = models.CharField(max_length=255, verbose_name="Alcance", null=True, blank=True)
    productos_entregables = models.CharField(max_length=255, verbose_name="Productos Entregables", null=True, blank=True)
    impacto_institucional = models.CharField(max_length=255, verbose_name="Impacto Institucional", null=True, blank=True)
    compromisos_de_las_partes = models.CharField(max_length=255, verbose_name="Compromisos de las Partes", null=True, blank=True)
    logros_alcanzados = models.CharField(max_length=255, verbose_name="Logros Alcanzados", null=True, blank=True)
    
    fecha_suscripcion = models.DateField(verbose_name="Fecha de Suscripción")

    # --- Archivos y Auditoría (Nuevos Campos) ---
    archivo = models.FileField(
        upload_to="instrCooperacion/",
        null=True, 
        blank=True,
        verbose_name="Documento PDF"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Modificación"
    )

    class Meta:
        verbose_name = "Instrumento de Cooperación"
        verbose_name_plural = "Instrumentos de Cooperación"
        ordering = ["-fecha_creacion"]

    def save(self, *args, **kwargs):
        if not self.codigo:
            ultimo = InstrumentoCooperacion.objects.order_by("-id").first()
            if ultimo:
                numero = ultimo.id + 1
            else:
                numero = 1
            # Formato solicitado: INCOOP00001
            self.codigo = f"INSCOOP-{numero:05d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.objeto if self.objeto else 'Sin Objeto'}"