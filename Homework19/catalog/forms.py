from django import forms
from catalog.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_disc', 'image', 'category', 'price', 'data_created', 'data_changed']