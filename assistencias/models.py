from django.db import models
from jogadores.models import Jogador
from partidas.models import Partida


class Assistencia(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT, null=True)
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.id)
