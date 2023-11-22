from django import forms
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


class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "number_address",
            "address",
            "zip_code",
            "city",
            "country",
        )


class PlaceCreationForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = (
            "name",
            "product",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control form-control",
                    "placeholder": "name",
                    "aria-label": "name",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PlaceCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            "name", "product", Submit("submit", "New Swapping Place")
        )


class PlaceAddressFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.nested = AddressCreationForm(prefix=f"address-{index}")


PlaceAddressFormSet = formset_factory(
    AddressCreationForm, formset=PlaceAddressFormSet, extra=1, can_delete=True
)
