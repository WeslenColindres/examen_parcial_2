from django.db import models

class Procurador(models.Model):
    dni = models.CharField(max_length=9)
    casos_ganados = models.DecimalField(max_digits=5, decimal_places=0)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero_colegiado = models.DecimalField(max_digits=5, decimal_places=0)

