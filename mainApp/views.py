from django.shortcuts import render
from rest_framework import filters, viewsets
from mainApp.serializers import ProductSerializer
from mainApp.models import Product
from django_filters import rest_framework

class ProductFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['color', 'brand', 'min_price', 'max_price']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = ProductFilter
    search_fields = ('price', 'color', 'brand',)
