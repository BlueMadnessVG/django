from enum import auto
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Project(models.Model):
    Nombre = models.CharField(max_length=200)
    Raza = models.CharField(max_length=200)