from django.db import models
from clubes.models import Clube
from rodadas.models import Rodada


class Partida(models.Model):
    clubes = models.ManyToManyField(Clube, max_length=2)
    rodada = models.ForeignKey(Rodada, on_delete=models.PROTECT, default=0)
    nome = models.TextField()

    def __str__(self):
        return self.nome
