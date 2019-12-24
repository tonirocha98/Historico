from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from clubes.models import Clube
from clubes.api.serializers import ClubeSerializer


class ClubeViewSet(ModelViewSet):
    serializer_class = ClubeSerializer
    filter_fields = ['ativo']# django_filter habilitado no settings
    filter_backends = [SearchFilter]
    search_fields = ['nome']
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # queryset = Clube.objects.all()

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        queryset = Clube.objects.all()

        if id:
          queryset = queryset.filter(pk=id)

        return queryset
        # return Clube.objects.filter(ativo=True)
        # return Clube.objects.filter(self.ativo=True)

    http_method_names = ['get', 'post']

    # detail | receber parametro via rota
    # true para metodos especificos da Jogador x
    @action(methods=['post'], detail=True)
    def adicionar_gol_partida(self, request, pk=None):
        return Response(self)

    # detail | receber parametro via rota
    # false para metodos que agem em todas as Jogadores
    @action(methods=['post'], detail=False)
    def adicionar(self, request):
        return Response(self)

    def list(self, request, *args, **kwargs):
        return super(ClubeViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ClubeViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ClubeViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ClubeViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ClubeViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ClubeViewSet, self).destroy(request, *args, **kwargs)
