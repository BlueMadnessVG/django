from django.db import models

# Create your models here.
class Project(models.Model):
    Nombre = models.CharField(max_length=200)
    Raza = models.CharField(max_length=200)