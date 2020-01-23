from django.db import models
from jogadores.models import Jogador
from estadios.models import Estadio


class Clube(models.Model):
    nome = models.TextField(default='')
    data_fundacao = models.DateTimeField(null=True)
    ativo = models.BooleanField(default=False)
    estadio = models.ForeignKey(Estadio, on_delete=models.DO_NOTHING, blank=True, null=True)
    foto = models.ImageField(upload_to='clubes', null=True, blank=True)
    jogadores = models.ManyToManyField(Jogador)

    def __str__(self):
        return self.nome