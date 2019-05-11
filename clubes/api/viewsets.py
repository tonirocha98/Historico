from rest_framework.viewsets import ModelViewSet
from clubes.models import Clube
from clubes.api.serializers import ClubeSerializer


class ClubeViewSet(ModelViewSet):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer
