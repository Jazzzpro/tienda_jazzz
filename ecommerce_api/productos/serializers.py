from rest_framework import serializers
from .models import Producto, Nota


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    reseñas = NotaSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'