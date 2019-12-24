from rest_framework.serializers import ModelSerializer
from clube_mandante.models import ClubeMandante


class ClubeMandanteSerializer(ModelSerializer):
    class Meta:
        model = ClubeMandante
        fields = ('id', 'nome')
