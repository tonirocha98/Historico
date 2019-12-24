from rest_framework.serializers import ModelSerializer
from historico.models import Historico


class HistoricoSerializer(ModelSerializer):
    class Meta:
        model = Historico
        fields = ('id', 'clube', 'partidas')
