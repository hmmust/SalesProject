from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from .models import Product,Supplier
from .forms import ProductForm, SupplierForm
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
def homepage(request):
    return HttpResponse("Welcome to home !")

class ProductAdd(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "add.html"
    success_url = reverse_lazy("homepage")

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "edit.html"
    success_url = reverse_lazy("homepage")

class ProductList(ListView):
    model = Product
    template_name = "homepage.html"
    success_url = reverse_lazy("homepage")
    context_object_name = "products"

class ProductDelete(DeleteView):
    model = Product
    template_name = "delete.html"
    success_url = reverse_lazy("homepage")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
