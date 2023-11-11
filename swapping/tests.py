from django.test import TestCase
from django.urls import reverse, resolve
from .models import SwappingProduct
from .views import SwappingProductListView, SwappingProductDetailView


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
        view = resolve("/swapping/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Short")
        self.assertTemplateUsed(response, "swapping/swapping_product_detail.html")
        self.assertEqual(
            view.func.__name__, SwappingProductDetailView.as_view().__name__
        )
