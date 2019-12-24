from rest_framework.serializers import ModelSerializer
from clubes_partidas.models import ClubePartida


class ClubePartidaSerializer(ModelSerializer):
    class Meta:
        model = ClubePartida
        fields = ('id', 'clube')
