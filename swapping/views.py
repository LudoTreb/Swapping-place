from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import SwappingProduct
from django.urls import reverse_lazy
from .forms import SwappingProductCreationForm
import logging

logger = logging.getLogger(__name__)


class SwappingProductListView(ListView):
    model = SwappingProduct
    context_object_name = "swapping_product_list"
    template_name = "swapping/swapping_product_list.html"


class SwappingProductDetailView(DetailView):
    model = SwappingProduct
    context_object_name = "swapping_product"
    template_name = "swapping/swapping_product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        swapping_place = context["swapping_product"].swappingplace_set
        print("hello")
        print(swapping_place)
        # Récupérer l'adresse du lieu
        address = swapping_place.address

        # Générez la carte et obtenez le succès
        success = get_on_map(address)

        # Ajoutez la variable 'success' au contexte
        context["success"] = success

        return context


class SwappingProductUpdateView(UpdateView):
    model = SwappingProduct
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

    # FIXME Problème de validation du formulaire avec le champ owner ne se rempli pas automatiquement avec le user connecté

    def form_valid(self, form):
        form.instance.owner = self.request.user
        logger.info(form.cleaned_data)
        print(form.is_valid())
        print(form.cleaned_data)
        print(form.errors)
        return super().form_valid(form)
