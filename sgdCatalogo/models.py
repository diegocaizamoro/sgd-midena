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


