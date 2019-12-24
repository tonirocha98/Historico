from rest_framework.serializers import ModelSerializer
from gols.models import Gol


class GolSerializer(ModelSerializer):
    class Meta:
        model = Gol
        fields = ('id', 'jogador', 'data', 'anulado')
