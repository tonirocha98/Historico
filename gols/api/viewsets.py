from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from gols.models import Gol
from gols.api.serializers import GolSerializer


class GolViewSet(ModelViewSet):
    serializer_class = GolSerializer
    # queryset = Gol.objects.all()

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        queryset = Gol.objects.all()

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
        return super(GolViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(GolViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(GolViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(GolViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(GolViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(GolViewSet, self).destroy(request, *args, **kwargs)
