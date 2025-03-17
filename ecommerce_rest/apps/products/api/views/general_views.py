from rest_framework import viewsets

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer,IndicatorSerializer

class MeasureUnitListAPIView(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

class CategoryProductListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer