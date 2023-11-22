from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView, HowItWorksPageView


class HomepageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Welcome to the SwappingPlace")

    def test_homepage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "i'm not suppose to be here!")

    def test_home_pageurl_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutpageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_url_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About")

    def test_aboutpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "I'm not suppose to be here")

    def test_about_pageurl_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)


class HowpageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("how")
        self.response = self.client.get(url)

    def test_url_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_howpage_template(self):
        self.assertTemplateUsed(self.response, "how.html")

    def test_howpage_contains_correct_html(self):
        self.assertContains(self.response, "How does it work?")

    def test_howpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "I'm not suppose to be here")

    def test_how_pageurl_resolves_howpageview(self):
        view = resolve("/how/")
        self.assertEqual(view.func.__name__, HowItWorksPageView.as_view().__name__)
