from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from gols.api.serializers import GolSerializer
from clubes.api.serializers import ClubeSerializer
# from clubes_partidas.api.serializers import ClubePartidaSerializer
from partidas.models import Partida


class PartidaSerializer(ModelSerializer):
    clubes = ClubeSerializer(many=True, read_only=False)
    gols = GolSerializer(many=True, read_only=False)
    estatisticas = SerializerMethodField()
    # clubes = ClubePartidaSerializer(many=True, read_only=True)

    class Meta:
        model = Partida
        fields = (
            'temporada', 'rodada', 'data_inicio', 'data_fim',
            'publico', 'estadio', 'clubes', 'gols',
            'estatisticas', 'estatisticas2'
        )

    def get_estatisticas(self, obj):
        return '%s - Rodada %s' % (obj.temporada.ano, obj.rodada.numero_rodada)