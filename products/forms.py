from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="name")
    description = forms.CharField(max_length=300, label="description")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="price")
    available = forms.BooleanField(initial=True, label="available", required=False)
    photo = forms.ImageField(label="Photo", required=False)
