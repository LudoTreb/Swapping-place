from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreationView,
    MyProductListView,
    PlaceCreationView,
)


urlpatterns = [
    path(
        "<uuid:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "<uuid:pk>/edit/",
        ProductUpdateView.as_view(),
        name="product_edit",
    ),
    path(
        "<uuid:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "new/",
        ProductCreationView.as_view(),
        name="product_new",
    ),
    path(
        "new-place/",
        PlaceCreationView.as_view(),
        name="place_new",
    ),
    path("", ProductListView.as_view(), name="product_list"),
    path("my-products", MyProductListView.as_view(), name="my_product_list"),
]
