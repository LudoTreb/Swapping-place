from django import forms
from iso3166 import countries
from django.forms import BaseFormSet
from django.forms import formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Product, Address, Place


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
                    "class": "form-control form-control",
                    "placeholder": "Title",
                    "aria-label": "Title",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "enctype": "multipart/form-data",
                    "aria-label": "Image",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                    "aria-label": "Category",
                    "placeholder": "Category",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column("title", css_class="form-group col-md-6"),
            Column("image", css_class="form-group col-md-6"),
            Row(
                Column("category", css_class="col-md-2"),
                Column("sex", css_class="col-md-2"),
                Column("size", css_class="col-md-2"),
            ),
            Row(
                Column("color", css_class="col-md-2"),
                Column("condition", css_class="col-md-2"),
                Column("quality", css_class="col-md-2"),
            ),
            Column("description", css_class="form-group col-md-6"),
            Submit("submit", "New"),
        )


class PlaceCreateForm(forms.ModelForm):
    number_address = forms.CharField(label="Number", help_text="number of the road")
    address = forms.CharField(label="Address", help_text="name of the road")
    zip_code = forms.CharField(label="Zip Code")
    city = forms.CharField(label="City")
    country = forms.ChoiceField(
        label="Country",
        choices=[("", "Select country")]
        + [(country.alpha2.lower(), country.name) for country in countries],
    )

    class Meta:
        model = Place
        fields = [
            "name",
            "number_address",
            "address",
            "zip_code",
            "city",
            "country",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control form-control",
                    "placeholder": "Name",
                    "aria-label": "Name",
                }
            ),
            "number_address": forms.TextInput(
                attrs={
                    "class": "form-control form-control",
                    "placeholder": "Number Address",
                    "aria-label": "number address",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control form-control",
                    "placeholder": "address",
                    "aria-label": "address",
                }
            ),
            "zip_code": forms.TextInput(
                attrs={
                    "class": "form-control form-control",
                    "placeholder": "zip_code",
                    "aria-label": "zip_code",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control form-control",
                    "placeholder": "city",
                    "aria-label": "city",
                }
            ),
            "country": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Country",
                    "aria-label": "Country",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column("name", css_class="form-group col-md-6"),
            Row(
                Column("number_address", css_class="form-group col-md-2"),
                Column("address", css_class="col-md-4"),
            ),
            Row(
                Column("zip_code", css_class="form-group col-md-2"),
                Column("city", css_class="form-group col-md-2"),
                Column("country", css_class="form-group col-md-2"),
            ),
            Submit("submit", "New Swapping Place"),
        )
