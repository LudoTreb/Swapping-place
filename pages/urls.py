from django.urls import path
from .views import HomePageView, AboutPageView, HowItWorksPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("how/", HowItWorksPageView.as_view(), name="how"),
    path("", HomePageView.as_view(), name="home"),
]
