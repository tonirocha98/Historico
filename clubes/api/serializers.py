from rest_framework.serializers import ModelSerializer
from clubes.models import Clube
from jogadores.api.serializers import JogadorSerializer


class ClubeSerializer(ModelSerializer):
    jogadores = JogadorSerializer(many=True)

    class Meta:
        model = Clube
        fields = ('id', 'nome', 'data_fundacao', 'ativo', 'estadio', 'foto', 'jogadores')
