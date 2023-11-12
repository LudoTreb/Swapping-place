from django.test import TestCase
from django.urls import reverse, resolve
from .models import SwappingProduct
from .views import (
    SwappingProductListView,
    SwappingProductDetailView,
    SwappingProductCreationView,
    SwappingProductUpdateView,
    SwappingProductDeleteView,
)


class SwappingProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.swapping_product = SwappingProduct.objects.create(
            title="Short",
            description="Très joli short",
            category="Clothing",
            sex="Women",
            size="S",
            product_condition="New",
            color="Silver",
            quality="Good",
        )

    def test_swapping_product_listing(self):
        self.assertEqual(self.swapping_product.title, "Short")
        self.assertEqual(self.swapping_product.description, "Très joli short")
        self.assertEqual(
            self.swapping_product.category,
            SwappingProduct.CategoryChoices.clothing,
        )
        self.assertEqual(
            self.swapping_product.sex,
            SwappingProduct.SexChoices.women,
        )
        self.assertEqual(
            self.swapping_product.size,
            SwappingProduct.SizeChoices.s,
        )
        self.assertEqual(
            self.swapping_product.product_condition,
            SwappingProduct.ProductConditionChoices.new,
        )
        self.assertEqual(
            self.swapping_product.color,
            SwappingProduct.ColorChoices.silver,
        )
        self.assertEqual(
            self.swapping_product.quality,
            SwappingProduct.QualityChoices.good,
        )

    def test_swapping_product_list_view(self):
        response = self.client.get(reverse("swapping_product_list"))
        view = resolve("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Short")
        self.assertTemplateUsed(response, "swapping/swapping_product_list.html")
        self.assertEqual(view.func.__name__, SwappingProductListView.as_view().__name__)

    def test_swapping_product_detail_view(self):
        response = self.client.get(self.swapping_product.get_absolute_url())
        view = resolve(f"/swapping/{self.swapping_product.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Short")
        self.assertTemplateUsed(response, "swapping/swapping_product_detail.html")
        self.assertEqual(
            view.func.__name__, SwappingProductDetailView.as_view().__name__
        )

    def test_swapping_product_update_view(self):
        response = self.client.get(
            reverse("swapping_product_edit", kwargs={"pk": self.swapping_product.pk})
        )
        view = resolve(f"/swapping/{self.swapping_product.pk}/edit/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit")
        self.assertTemplateUsed(response, "swapping/swapping_product_edit.html")
        self.assertEqual(
            view.func.__name__, SwappingProductUpdateView.as_view().__name__
        )

    def test_swapping_product_delete_view(self):
        response = self.client.get(
            reverse("swapping_product_delete", kwargs={"pk": self.swapping_product.pk})
        )
        view = resolve(f"/swapping/{self.swapping_product.pk}/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure you want to delete your product:")
        self.assertTemplateUsed(response, "swapping/swapping_product_delete.html")
        self.assertEqual(
            view.func.__name__, SwappingProductDeleteView.as_view().__name__
        )

    def test_swapping_product_create_view(self):
        response = self.client.get(reverse("swapping_product_new"))
        view = resolve("/swapping/new/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New clothe")
        self.assertTemplateUsed(response, "swapping/swapping_product_new.html")
        self.assertEqual(
            view.func.__name__, SwappingProductCreationView.as_view().__name__
        )

    def test_swapping_product_create_new_clothe(self):
        new_clothe_data = {
            "title": "Jogging",
            "description": "Très confort",
            "category": SwappingProduct.CategoryChoices.clothing,
            "sex": SwappingProduct.SexChoices.women,
            "size": SwappingProduct.SizeChoices.l,
            "color": SwappingProduct.ColorChoices.red,
            "product_condition": SwappingProduct.ProductConditionChoices.fair_condition,
            "quality": SwappingProduct.QualityChoices.good,
        }
        response = self.client.post(reverse("swapping_product_new"), new_clothe_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("swapping_product_list"))
        self.assertTrue(SwappingProduct.objects.filter(title="Jogging").exists())
