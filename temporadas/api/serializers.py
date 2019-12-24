from rest_framework.serializers import ModelSerializer
from temporadas.models import Temporada


class TemporadaSerializer(ModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id', 'nome')
