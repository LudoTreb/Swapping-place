from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import SwappingProduct
from django.urls import reverse_lazy
from .forms import SwappingProductCreationForm


class SwappingProductListView(ListView):
    model = SwappingProduct
    context_object_name = "swapping_product_list"
    template_name = "swapping/swapping_product_list.html"


class SwappingProductDetailView(DetailView):
    model = SwappingProduct
    context_object_name = "swapping_product"
    template_name = "swapping/swapping_product_detail.html"


class SwappingProductUpdateView(UpdateView):
    model = SwappingProduct
    fields = (
        "title",
        "category",
        "sex",
        "size",
        "color",
        "description",
        "product_condition",
        "quality",
    )
    template_name = "swapping/swapping_product_edit.html"


class SwappingProductDeleteView(DeleteView):
    model = SwappingProduct
    context_object_name = "swapping_product"
    template_name = "swapping/swapping_product_delete.html"
    success_url = reverse_lazy("swapping_product_list")


class SwappingProductCreationView(CreateView):
    model = SwappingProduct
    form_class = SwappingProductCreationForm
    template_name = "swapping/swapping_product_new.html"
    success_url = reverse_lazy("swapping_product_list")
