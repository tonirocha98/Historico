from rest_framework.serializers import ModelSerializer
from clubes.models import Clube


class ClubeSerializer(ModelSerializer):
    class Meta:
        model = Clube
        fields = ('id', 'nome')
