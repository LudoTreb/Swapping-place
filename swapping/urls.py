from django.urls import path
from .views import (
    SwappingProductListView,
    SwappingProductDetailView,
    SwappingProductUpdateView,
    SwappingProductDeleteView,
    SwappingProductCreationView,
)


urlpatterns = [
    path(
        "<int:pk>/", SwappingProductDetailView.as_view(), name="swapping_product_detail"
    ),
    path(
        "<int:pk>/edit/",
        SwappingProductUpdateView.as_view(),
        name="swapping_product_edit",
    ),
    path(
        "<int:pk>/delete/",
        SwappingProductDeleteView.as_view(),
        name="swapping_product_delete",
    ),
    path(
        "new/",
        SwappingProductCreationView.as_view(),
        name="swapping_product_new",
    ),
    path("", SwappingProductListView.as_view(), name="swapping_product_list"),
]
