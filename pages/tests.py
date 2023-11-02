from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomepageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "swapping place home")

    def test_homepage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "i'm not suppose to be here!")

    def test_home_pageurl_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
