from django.urls import path
from .views import SwappingProductListView


urlpatterns = [
    path("", SwappingProductListView.as_view(), name="swapping_product_list")
]
