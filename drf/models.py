from django.db import models

# Create your models here.

class Pais(models.Model):
    moneda= models.CharField(max_length=20)
    nombre= models.CharField(max_length=20)
    creado_en= models.DateTimeField(auto_now_add=True)

