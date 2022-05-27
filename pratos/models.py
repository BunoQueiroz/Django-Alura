from django.db import models

class Pratos(models.Model):
    nome_prato = models.CharField(max_length=70)
    principal = models.CharField(max_length=50)
    acompanhamento = models.TextField()
    tempo_medio_preparo = models.IntegerField()
    serve_ate = models.CharField(max_length=70)
    categoria = models.CharField(max_length=50)