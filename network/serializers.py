from rest_framework import serializers
from network.models import NetworkUnit, Product

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkUnit
        fields = '__all__'
        read_only_fields = ['debt', 'date_create']  # Поля, доступные только для чтения

class UnitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkUnit
        exclude = ['debt', 'date_create']  # Исключаемые поля, которые не должны быть доступны для обновления

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1  # Глубина вложенности для связанных объектов