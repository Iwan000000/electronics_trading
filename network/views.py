from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from network.models import NetworkUnit, Product
from network.serializers import UnitSerializer, UnitUpdateSerializer, ProductSerializer
from users.permissions import IsActiveUser


class UnitCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания объекта сети """
    serializer_class = UnitSerializer
    permission_classes = [IsActiveUser]


class UnitListAPIView(generics.ListAPIView):
    """ Контроллер для просмотра списка объектов сети """
    serializer_class = UnitSerializer
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class UnitRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра объекта сети """
    serializer_class = UnitSerializer
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsActiveUser]


class UnitUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения объекта сети """
    serializer_class = UnitUpdateSerializer
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsActiveUser]


class UnitDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления объекта сети """
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsActiveUser]


class ProductViewSet(viewsets.ModelViewSet):
    """ Контроллер для управления моделью Продукты """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
