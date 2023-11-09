from django.urls import path
from .views import SwappingProductListView, SwappingProductDetailView


urlpatterns = [
    path("", SwappingProductListView.as_view(), name="swapping_product_list"),
    path(
        "<int:pk>/", SwappingProductDetailView.as_view(), name="swapping_product_detail"
    ),
]
