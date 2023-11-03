from django.views.generic import ListView
from .models import SwappingProduct


class SwappingProductListView(ListView):
    model = SwappingProduct
    context_object_name = "swapping_product_list"
    template_name = "swapping/swapping_product_list.html"
