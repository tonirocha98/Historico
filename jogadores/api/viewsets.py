from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from jogadores.models import Jogador
from jogadores.api.serializers import JogadorSerializer


class JogadorViewSet(ModelViewSet):
    # queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

    def get_queryset(self):
        return Jogador.objects.all()
        # return Jogador.objects.filter(self.ativo=True)

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
        return Response(self)

    def create(self, request, *args, **kwargs):
        return super(JogadorViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(JogadorViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(JogadorViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(JogadorViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(JogadorViewSet, self).create(request, *args, **kwargs)
