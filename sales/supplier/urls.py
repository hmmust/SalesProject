
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="homepage"),
    path("add/", views.ProductAdd.as_view(), name="add"),
]
