from rest_framework.serializers import ModelSerializer
from assistencias.models import Assistencia


class AssistenciaSerializer(ModelSerializer):
    class Meta:
        model = Assistencia
        fields = ('id', 'nome')
