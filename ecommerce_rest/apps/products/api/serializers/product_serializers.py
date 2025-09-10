from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):
    measure_unit = MeasureUnitSerializer
    category_product = CategoryProductSerializer

    class Meta:
        model = Product
        exclude = ('state','created_date','modify_date','delete_data')
    
    def validate_measure_unit(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Debe ingresar una unidad de medida')
        return value 
    
    def validate_category_product(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Debe ingresar una categoría de producto')
        return 
    
    def validate(self, data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({
                'measure_unit': 'Debe ingresar una unidad de medida'
            })
        if 'category_product' not in data.keys():
            raise serializers.ValidationError({
                'category_product': 'Debe ingresar una categoría de producto'
            })
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }