from rest_framework.serializers import ModelSerializer
from partidas.models import Partida


class PartidaSerializer(ModelSerializer):
    class Meta:
        model = Partida
        fields = ('id', 'nome')
