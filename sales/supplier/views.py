from django.shortcuts import render,HttpResponse
from products.models import Product,Supplier
from products.forms import ProductForm, SupplierForm
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy

def homepage(request):
    return HttpResponse("Welcome to Supplier Home !")

class SupplierAdd(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "add.html"
    success_url = reverse_lazy("homepage")

class SupplierView(ListView):
    model = Supplier
    form_class = SupplierForm
    template_name = "base.html"
    success_url = reverse_lazy("homepage")

