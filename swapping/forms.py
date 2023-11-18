from django import forms
from .models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "title",
            "image",
            "category",
            "sex",
            "size",
            "color",
            "condition",
            "quality",
            "description",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "placeholder": "Title",
                    "aria-label": "Title",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "aria-label": "Image",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                    "aria-label": "Category",
                },
                choices=Product.CategoryChoices.choices,
            ),
            "sex": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Sex",
                    "aria-label": "Sex",
                },
                choices=Product.SexChoices.choices,
            ),
            "size": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Size",
                    "aria-label": "Size",
                },
                choices=Product.SizeChoices.choices,
            ),
            "color": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Color",
                    "aria-label": "Color",
                },
                choices=Product.ColorChoices.choices,
            ),
            "condition": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Condition",
                    "aria-label": "Condition",
                },
                choices=Product.ConditionChoices.choices,
            ),
            "quality": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Quality",
                    "aria-label": "Quality",
                },
                choices=Product.QualityChoices.choices,
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control form-control-sm",
                    "placeholder": "Description",
                    "aria-label": "Description",
                }
            ),
        }
