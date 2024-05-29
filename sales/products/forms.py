import django.core.exceptions
from django import forms
from .models import Product,Supplier
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets ={"purchase_date":forms.NumberInput(attrs={"type":"date"}),"description":forms.TextInput()}

    def clean_quantity(self):
        if int(self.cleaned_data['quantity']) <0:
            raise django.core.exceptions.ValidationError("Quantity must be greater or equal zero")
        return self.cleaned_data['quantity']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["sid","name"]

