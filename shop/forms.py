from django import forms
from shop.models import Product
from django.utils import timezone


class ProductAddForm(forms.ModelForm):
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 10,
                'cols': 30,
                'placeholder': 'Product description'
            }
        ),
    )
    add_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'value': timezone.localdate(),
                'readonly': 'true'
            }
        )
    )
    product_name = forms.CharField(

        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product'
            }
        )
    )

    class Meta:
        model = Product
        exclude = [
            'expired',
            'user'
        ]

