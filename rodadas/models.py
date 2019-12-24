from django.db import models
# from partidas.models import Partida
from temporadas.models import Temporada


class Rodada(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    temporada = models.ForeignKey(Temporada, on_delete=models.PROTECT, default=0)
    numero_rodada = models.IntegerField(default=0, blank=False)
    # Partida = models.ForeignKey(Partida, on_delete=models.PROTECT, default=0, null=True)

    def __str__(self):
        return str(self.id)
