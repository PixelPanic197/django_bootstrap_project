# products/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['article', 'status', 'sku', 'confirmation_date', 'comment']