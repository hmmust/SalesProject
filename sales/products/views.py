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
    success_url = reverse_lazy("products:homepage")

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "edit.html"
    success_url = reverse_lazy("products:homepage")

class ProductList(ListView):
    model = Product
    template_name = "homepage.html"
    success_url = reverse_lazy("products:homepage")
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        return  Product.objects.filter(supplier=Supplier.objects.get(name="Hossam")).order_by("name")

class ProductDelete(DeleteView):
    model = Product
    template_name = "delete.html"
    success_url = reverse_lazy("products:homepage")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
