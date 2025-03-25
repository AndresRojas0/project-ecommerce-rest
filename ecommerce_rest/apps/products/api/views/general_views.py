from rest_framework import viewsets

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer,IndicatorSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer