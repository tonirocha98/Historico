from rest_framework.viewsets import ModelViewSet
from assistencias.models import Assistencia
from assistencias.api.serializers import AssistenciaSerializer


class AssistenciaViewSet(ModelViewSet):
    queryset = Assistencia.objects.all()
    serializer_class = AssistenciaSerializer
