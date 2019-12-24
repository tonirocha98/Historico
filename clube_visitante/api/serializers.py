from rest_framework.serializers import ModelSerializer
from clube_visitante.models import ClubeVisitante


class ClubeVisitanteSerializer(ModelSerializer):
    class Meta:
        model = ClubeVisitante
        fields = ('id', 'nome')
