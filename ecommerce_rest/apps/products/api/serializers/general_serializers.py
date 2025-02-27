from apps.products.models import MeasureUnit,CategoryProduct,Indicator

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state','created_date','modify_date','delete_data')

class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ('state','created_date','modify_date','delete_data')

class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state','created_date','modify_date','delete_data')