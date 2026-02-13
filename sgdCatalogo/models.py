from django.db import models

class KnowledgeDocumentType(models.Model):
    name = models.CharField(max_length=150,verbose_name=("Nombre"))
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Tipo de documento")
        verbose_name_plural = ("Tipos documentales")

    
class KnowledgeDocumentStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ReferenceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class StrategicCapability(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class KnowledgeArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ResearchLine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Institution(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
class ResearchNetwork(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Expert(models.Model):
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class RedesInvestigacion(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Red de Investigación"
        verbose_name_plural = "Redes de Investigación"

    def __str__(self):
        return self.name


class AplicacionPotencial(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Aplicación Potencial"
        verbose_name_plural = "Aplicaciones Potenciales"

    def __str__(self):
        return self.name


class Referencia(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"

    def __str__(self):
        return self.name
    
class NivelSeguridad(models.Model):  #cambio de diego
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Nivel Seguridad"
        verbose_name_plural = "Niveles de Seguridad"

    def __str__(self):
        return self.name
