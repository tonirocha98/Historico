from rest_framework.serializers import ModelSerializer
from estadios.models import Estadio


class EstadioSerializer(ModelSerializer):
    class Meta:
        model = Estadio
        fields = ('id', 'nome', 'data_fundacao')
