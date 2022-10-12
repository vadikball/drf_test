from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.schemas.openapi import AutoSchema

from cars.models import Color, Brand, CarModel, Order
from cars.serializers import (ColorSerializer,
                              BrandSerializer,
                              CarModelSerializer,
                              OrderSerializer,
                              OrderedColorSerializer,
                              OrderedBrandSerializer)


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related().all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('car_model__brand', )
    ordering_fields = ('date', 'amount', )
    ordering = 'date'


class OrderedColorViewSet(viewsets.ReadOnlyModelViewSet):
    schema = AutoSchema(
        operation_id_base='OrderedColor',
    )
    queryset = Color.objects.all()
    serializer_class = OrderedColorSerializer


class OrderedBrandViewSet(viewsets.ReadOnlyModelViewSet):
    schema = AutoSchema(
        operation_id_base='OrderedBrand',
    )
    queryset = Brand.objects.all()
    serializer_class = OrderedBrandSerializer
