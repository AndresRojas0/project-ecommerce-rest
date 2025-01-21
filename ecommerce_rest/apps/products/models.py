from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class MeasureUnit(BaseModel):

    description = models.CharField('Descripción', max_length=50,blank=False,null=False,unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plurar = 'Unidades de Medida'
    
    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):
    description = models.CharField('Descripción', max_length=50,blank=False,null=False,unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    historial = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plurar = 'Categorías de Productos'

    def __str__(self):
        return self.description

class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default = 0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plurar = 'Indicadores de Oferta'
    
    def __str__(self):
        return self.descount_value