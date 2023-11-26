from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Product, Place
from django.urls import reverse_lazy
from .forms import (
    ProductCreationForm,
    PlaceCreateForm,
)


class ProductListView(ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "swapping/product_list.html"


class MyProductListView(ListView):
    model = Product
    context_object_name = "my_product_list"
    template_name = "swapping/my_product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer la Place associée à l'utilisateur actuel
        user_places = Place.objects.filter(owner=self.request.user)

        # Vérifier si l'utilisateur a au moins une Place
        if user_places.exists():
            # Passer le nom de la première place au contexte
            context["places"] = user_places

        return context

    def get_queryset(self):
        # Récupérer la Place associée à l'utilisateur actuel
        user_places = Place.objects.filter(owner=self.request.user)

        # Vérifier si l'utilisateur a au moins une Place
        if user_places.exists():
            # Récupérer les produits associés à toutes les places
            place_products = Product.objects.filter(places__in=user_places)
            return place_products
        else:
            # Si l'utilisateur n'a pas de Place, retourner une queryset vide
            return Product.objects.none()


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


class PlaceCreateView(CreateView):
    model = Place
    form_class = PlaceCreateForm
    template_name = "swapping/place_new.html"
    success_url = reverse_lazy("my_product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
