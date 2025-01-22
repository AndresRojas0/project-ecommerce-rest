from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer,IndicatorSerializer

class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer

class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer