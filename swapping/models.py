from django.db import models


class SwappingProduct(models.Model):
    class CategoryChoices(models.TextChoices):
        clothing = 'Clothing', 'clothing'
        shoes = 'Shoes', 'shoes'

    class SexChoices(models.TextChoices):
        women = 'Women', 'women'
        man = 'Man', 'man'
        kid = 'Kid', 'kid'

    class SizeChoices(models.TextChoices):
        XS = 'XS', 'xs'
        S = 'S', 's'
        M = 'M', 'm'
        L = 'L', 'l'
        XL = 'XL', 'xl'
        XXL = 'XXL', 'xxl'

    class ProductConditionChoices(models.TextChoices):
        new = 'New', 'new'
        as_new = 'As new', 'as new'
        very_good_condition = 'Very good condition', 'very good condition'
        good_condition = 'Good condition', 'good condition'
        fair_condition = 'Fair condition', 'fair condition'
        worn = 'Worn', 'worn'

    class ColorChoices(models.TextChoices):
        black = 'Black', 'black'
        white = 'White', 'white'
        red = 'Red', 'red'
        green = 'Green', 'green'
        blue = 'Blue', 'blue'
        yellow = 'Yellow', 'yellow'
        orange = 'Orange', 'orange'
        pink = 'Pink', 'pink'
        purple = 'Purple', 'purple'
        brown = 'Brown', 'brown'
        silver = 'Silver', 'silver'
        gold = 'Gold', 'gold'

    class QualityChoices(models.TextChoices):
        poor = 'Poor', 'poor'
        low_quality = 'Low-quality', 'low-quality'
        good = 'Good', 'good'
        excellent = 'Excellent', 'excellent'
        luxurious = 'Luxurious', 'luxurious'
        custom_made = 'Custom-made', 'custom-made'

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=20, choices=CategoryChoices.choices)
    sex = models.CharField(max_length=8, choices=SexChoices.choices)
    size = models.CharField(max_length=3, choices=SizeChoices.choices)
    product_condition = models.CharField(
        max_length=25, choices=ProductConditionChoices.choices
    )
    color = models.CharField(max_length=20, choices=ColorChoices.choices)
    quality = models.CharField(max_length=20, choices=QualityChoices.choices)

    def __str__(self):
        return self.title
