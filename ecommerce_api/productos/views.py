from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria']
    search_fields = ['nombre']

    @action(detail=False, methods=['get'])
    def solo_stock(self, request):
        productos = self.filter_queryset(self.get_queryset().filter(stock=True))
        page = self.paginate_queryset(productos)
        if page is not None:
            serializer = ProductoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)