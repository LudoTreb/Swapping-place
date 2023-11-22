from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Product, Place
from django.urls import reverse_lazy
from .forms import (
    ProductCreationForm,
    PlaceCreationForm,
    AddressCreationForm,
    PlaceAddressFormSet,
)
import logging

logger = logging.getLogger(__name__)


class ProductListView(ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "swapping/product_list.html"


class MyProductListView(ListView):
    model = Product
    context_object_name = "my_product_list"
    template_name = "swapping/my_product_list.html"

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user.id)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "swapping/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        place = context["product"].places.get()

        # Générez la carte et obtenez le succès
        success = place.get_on_map()

        # Ajoutez la variable 'success' au contexte
        context["success"] = success

        return context


class ProductUpdateView(UpdateView):
    model = Product
    fields = (
        "title",
        "category",
        "sex",
        "size",
        "color",
        "description",
        "condition",
        "quality",
    )
    template_name = "swapping/product_edit.html"


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = "product"
    template_name = "swapping/product_delete.html"
    success_url = reverse_lazy("product_list")


class ProductCreationView(CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = "swapping/product_new.html"
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PlaceCreationView(CreateView):
    model = Place
    form_class = PlaceCreationForm
    template_name = "swapping/place_new.html"
    success_url = reverse_lazy("my_product_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["addresses"] = PlaceAddressFormSet(self.request.POST, prefix="address")
        else:
            data["addresses"] = PlaceAddressFormSet(prefix="address")
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        addresses = context["addresses"]
        with transaction.atomic():
            form.instance.owner = self.request.user
            self.object = form.save()

            if addresses.is_valid():
                for address_form in addresses:
                    address = address_form.save(commit=False)
                    address.place = self.object
                    address.save()

        return super().form_valid(form)
