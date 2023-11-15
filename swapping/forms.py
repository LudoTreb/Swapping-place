from django import forms
from .models import SwappingProduct


class SwappingProductCreationForm(forms.ModelForm):
    class Meta:
        model = SwappingProduct
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
            "owner",
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
                choices=SwappingProduct.CategoryChoices.choices,
            ),
            "sex": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Sex",
                    "aria-label": "Sex",
                },
                choices=SwappingProduct.SexChoices.choices,
            ),
            "size": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Size",
                    "aria-label": "Size",
                },
                choices=SwappingProduct.SizeChoices.choices,
            ),
            "color": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Color",
                    "aria-label": "Color",
                },
                choices=SwappingProduct.ColorChoices.choices,
            ),
            "condition": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Condition",
                    "aria-label": "Condition",
                },
                choices=SwappingProduct.ConditionChoices.choices,
            ),
            "quality": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Quality",
                    "aria-label": "Quality",
                },
                choices=SwappingProduct.QualityChoices.choices,
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control form-control-sm",
                    "placeholder": "Description",
                    "aria-label": "Description",
                }
            ),
        }
