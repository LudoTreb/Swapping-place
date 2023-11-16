import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from iso3166 import countries
from geopy.geocoders import Nominatim


class Product(models.Model):
    """
    Model representing a clothing
    item that the user will add to his store
    """

    class CategoryChoices(models.TextChoices):
        CLOTHING = "clothing", "Clothing"
        SHOES = "shoes", "Shoes"

    class SexChoices(models.TextChoices):
        WOMEN = "women", "Women"
        MAN = "man", "Man"
        KID = "kid", "Kid"

    class SizeChoices(models.TextChoices):
        XS = "xs", "XS"
        S = "s", "S"
        M = "m", "M"
        L = "l", "L"
        XL = "xl", "XL"
        XXL = "xxl", "XXL"

    class ConditionChoices(models.TextChoices):
        NEW = "new", "Brand New"
        AS_NEW = "as_new", "As New"
        VERY_GOOD = "very_goog", "Very Good Condition"
        GOOD = "good", "Good Condition"
        FAIR = "fair", "Fair Condition"
        WORN = "worn", "Worn"

    class ColorChoices(models.TextChoices):
        BLACK = "black", "Black"
        WHITE = "white", "White"
        RED = "red", "Red"
        GREEN = "green", "Green"
        BLUE = "blue", "Blue"
        YELLOW = "yellow", "Yellow"
        ORANGE = "orange", "Orange"
        PINK = "pink", "Pink"
        PURPLE = "purple", "Purple"
        BROWN = "brown", "Brown"
        SILVER = "silver", "Silver"
        GOLD = "gold", "Gold"

    class QualityChoices(models.TextChoices):
        POOR = "poor", "Poor"
        LOW = "low_quality", "Low Quality"
        GOOD = "good", "Good"
        EXCELLENT = "excellent", "Excellent"
        LUXURIOUS = "Luxurious", "Luxurious"
        CUSTOM_MADE = "custom_made", "Custom-Made"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=20, choices=CategoryChoices.choices)
    sex = models.CharField(max_length=8, choices=SexChoices.choices)
    size = models.CharField(max_length=3, choices=SizeChoices.choices)
    condition = models.CharField(max_length=25, choices=ConditionChoices.choices)
    color = models.CharField(max_length=20, choices=ColorChoices.choices)
    quality = models.CharField(max_length=20, choices=QualityChoices.choices)
    is_favorite = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images_article/")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.id)])

    def how_long(self):
        """Calculte since the product was posted"""
        now = timezone.now()
        time_difference = now - self.created_date

        days, seconds = divmod(time_difference.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        if days >= 1:
            return f"{int(days)} days ago"
        elif hours >= 1:
            return f"{int(hours)} hours ago"
        elif minutes >= 1:
            return f"{int(minutes)} minutes ago"
        else:
            return "less than a minute"


class Address(models.Model):
    """An Model of address"""

    number_address = models.CharField(max_length=20, help_text="Number")
    address = models.CharField(max_length=1024, help_text="Address, road")
    zip_code = models.CharField(max_length=32)
    city = models.CharField(max_length=1024)
    country = models.CharField(
        max_length=2,
        choices=[(country.alpha2.lower(), country.name) for country in countries],
    )

    def __str__(self):
        data = self.__dict__.copy()
        data.update(country=self.get_country_display().upper())
        return f"{self.number_address} {self.address} {self.zip_code} {self.city} {data['country']}"


class Place(models.Model):
    """Create a model of shop associate with an user and an address"""

    name = models.CharField(max_length=30)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="places"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="places"
    )
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name="places"
    )

    def __str__(self):
        return self.name

    def get_coordinates(self):
        """Get coordinates, latitude & longitude from an address"""
        geolocator = Nominatim(user_agent="swapping_place")
        location = geolocator.geocode(self.address)
        return location.latitude, location.longitude

    def get_on_map(self):
        """create a map to locate the shop"""
        coordinates = get_coordinates()
        if coordinates:
            map_object = folium.Map(location=coordinates, zoom_start=15)
            folium.Marker(location=coordinates, popup=address).add_to(map_object)
            map_object.save("map.html")
            return True
        return False
