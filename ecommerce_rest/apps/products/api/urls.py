from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView,IndicatorListAPIView,CategoryProductListAPIView
from apps.products.api.views.product_views import (
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('measure_unit/',MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/',IndicatorListAPIView.as_view(), name = 'indicator'),
    path('category_product/',CategoryProductListAPIView.as_view(), name = 'category_product'),
    path('product/',ProductListCreateAPIView.as_view(), name = 'product'),
    path('product/retrieve-update-destroy/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view(), name = 'product-retrieve-update-destroy'),
]