from django.db import models
from clubes.models import Clube
# from clubes_partidas.models import ClubePartida
# from clube_mandante.models import ClubeMandante
# from clube_visitante.models import ClubeVisitante
from temporadas.models import Temporada
from rodadas.models import Rodada
from gols.models import Gol
from estadios.models import Estadio
from jogadores.models import Jogador


class Partida(models.Model):
    data_inicio = models.DateTimeField(null=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    publico = models.IntegerField(null=True, blank=True)
    # clubes = models.ManyToManyField(ClubePartida, max_length=2)
    clubes = models.ManyToManyField(Clube)
    gols = models.ManyToManyField(Gol)
    melhor_jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT, blank=True, null=True)
    temporada = models.ForeignKey(Temporada, on_delete=models.PROTECT, null=True)
    rodada = models.ForeignKey(Rodada, on_delete=models.PROTECT, null=True)
    estadio = models.ForeignKey(Estadio, on_delete=models.PROTECT, blank=True, null=True)

    # clube_mandante = models.ForeignKey(ClubeMandante, on_delete=models.PROTECT, default=0)
    # clube_mandante = ClubePartida()
    # clube_visitante = ClubePartida()
    # clube_visitante = models.ForeignKey(ClubeVisitante, on_delete=models.PROTECT, default=0)

    # metodo pode ser utilizado no campo FIELD do serializer
    @property
    def estatisticas2(self):
        return '%s - Rodada %s' % (self.temporada.ano, self.rodada.numero_rodada)

    # constructor
    def __str__(self):
         # if self.clubes:
            #
            # for item in self.clubes:
            #     if item.isMandante:
            #         clube_mandante = item.clube
            #     else:
            #         clube_visitante = item.clube

         #    return "%s - Rodada %s | %s vs %s" % (self.temporada.ano, self.rodada.numero_rodada, clube_mandante, clube_visitante)
         # else:
            return "%s - Rodada %s" % (self.temporada.ano, self.rodada.numero_rodada)