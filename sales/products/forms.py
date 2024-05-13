import django.core.exceptions
from django import forms
from .models import Product,Supplier
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets ={"purchase_date":forms.NumberInput(attrs={"type":"date"}),"description":forms.TextInput()}

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["sid","name"]

