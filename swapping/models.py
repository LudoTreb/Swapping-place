import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings


class SwappingProduct(models.Model):
    """
    Model representing a clothing
    item that the user will add to his store
    """

    class CategoryChoices(models.TextChoices):
        clothing = "Clothing", "clothing"
        shoes = "Shoes", "shoes"

    class SexChoices(models.TextChoices):
        women = "Women", "women"
        man = "Man", "man"
        kid = "Kid", "kid"

    class SizeChoices(models.TextChoices):
        xs = "XS", "xs"
        s = "S", "s"
        m = "M", "m"
        l = "L", "l"
        xl = "XL", "xl"
        xxl = "XXL", "xxl"

    class ConditionChoices(models.TextChoices):
        new = "New", "new"
        as_new = "As new", "as new"
        very_good_condition = "Very good condition", "very good condition"
        good_condition = "Good condition", "good condition"
        fair_condition = "Fair condition", "fair condition"
        worn = "Worn", "worn"

    class ColorChoices(models.TextChoices):
        black = "Black", "black"
        white = "White", "white"
        red = "Red", "red"
        green = "Green", "green"
        blue = "Blue", "blue"
        yellow = "Yellow", "yellow"
        orange = "Orange", "orange"
        pink = "Pink", "pink"
        purple = "Purple", "purple"
        brown = "Brown", "brown"
        silver = "Silver", "silver"
        gold = "Gold", "gold"

    class QualityChoices(models.TextChoices):
        poor = "Poor", "poor"
        low_quality = "Low-quality", "low-quality"
        good = "Good", "good"
        excellent = "Excellent", "excellent"
        luxurious = "Luxurious", "luxurious"
        custom_made = "Custom-made", "custom-made"

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
        return reverse("swapping_product_detail", args=[str(self.id)])
