from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .models import Product
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreationView,
    ProductUpdateView,
    ProductDeleteView,
)


class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(
            username="ludo",
            email="ludo@email.com",
            password="testpass123",
        )
        cls.product = Product.objects.create(
            title="Short",
            description="Très joli short",
            category="clothing",
            sex="women",
            size="s",
            condition="new",
            color="silver",
            quality="good",
            owner=user,
        )

    def test_product_listing(self):
        self.assertEqual(self.product.title, "Short")
        self.assertEqual(self.product.description, "Très joli short")
        self.assertEqual(
            self.product.category,
            Product.CategoryChoices.CLOTHING,
        )
        self.assertEqual(
            self.product.sex,
            Product.SexChoices.WOMEN,
        )
        self.assertEqual(
            self.product.size,
            Product.SizeChoices.S,
        )
        self.assertEqual(
            self.product.condition,
            Product.ConditionChoices.NEW,
        )
        self.assertEqual(
            self.product.color,
            Product.ColorChoices.SILVER,
        )
        self.assertEqual(
            self.product.quality,
            Product.QualityChoices.GOOD,
        )

    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))
        view = resolve("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Short")
        self.assertTemplateUsed(response, "swapping/product_list.html")
        self.assertEqual(view.func.__name__, ProductListView.as_view().__name__)

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        view = resolve(f"/swapping/{self.product.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Short")
        self.assertTemplateUsed(response, "swapping/product_detail.html")
        self.assertEqual(view.func.__name__, ProductDetailView.as_view().__name__)

    def test_product_update_view(self):
        response = self.client.get(
            reverse("product_edit", kwargs={"pk": self.product.pk})
        )
        view = resolve(f"/swapping/{self.product.pk}/edit/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit")
        self.assertTemplateUsed(response, "swapping/product_edit.html")
        self.assertEqual(view.func.__name__, ProductUpdateView.as_view().__name__)

    def test_product_delete_view(self):
        response = self.client.get(
            reverse("product_delete", kwargs={"pk": self.product.pk})
        )
        view = resolve(f"/swapping/{self.product.pk}/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure you want to delete your product:")
        self.assertTemplateUsed(response, "swapping/product_delete.html")
        self.assertEqual(view.func.__name__, ProductDeleteView.as_view().__name__)

    def test_product_create_view(self):
        response = self.client.get(reverse("product_new"))
        view = resolve("/swapping/new/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New clothe")
        self.assertTemplateUsed(response, "swapping/product_new.html")
        self.assertEqual(view.func.__name__, ProductCreationView.as_view().__name__)

    def test_product_create_new_clothe(self):
        new_clothe_data = {
            "title": "Jogging",
            "description": "Très confort",
            "category": Product.CategoryChoices.CLOTHING,
            "sex": Product.SexChoices.WOMEN,
            "size": Product.SizeChoices.L,
            "color": Product.ColorChoices.RED,
            "condition": Product.ConditionChoices.FAIR,
            "quality": Product.QualityChoices.GOOD,
        }
        response = self.client.post(reverse("product_new"), new_clothe_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("product_list"))
        self.assertTrue(Product.objects.filter(title="Jogging").exists())
