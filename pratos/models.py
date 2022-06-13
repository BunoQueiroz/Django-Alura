from django.db import models
from pessoas.models import Pessoa
from datetime import datetime

class Prato(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_prato = models.CharField(max_length=70)
    principal = models.CharField(max_length=50)
    acompanhamento = models.TextField()
    tempo_medio_preparo = models.IntegerField()
    serve_ate = models.CharField(max_length=70)
    categoria = models.CharField(max_length=50)
    publicada = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=datetime.now())
    foto_prato = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

    def __str__(self):
        return self.nome_prato