from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.products.models import MeasureUnit
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer,IndicatorSerializer

class MeasureUnitViewSet(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self,request):
        data = self.get_queryset()
        data = self.get_serializer(data,many = True)
        return Response(data.data)

class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer