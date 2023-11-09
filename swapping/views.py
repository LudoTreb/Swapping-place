from django.views.generic import ListView, DetailView
from .models import SwappingProduct


class SwappingProductListView(ListView):
    model = SwappingProduct
    context_object_name = "swapping_product_list"
    template_name = "swapping/swapping_product_list.html"


class SwappingProductDetailView(DetailView):
    model = SwappingProduct
    context_object_name = "swapping_product"
    template_name = "swapping/swapping_product_detail.html"
