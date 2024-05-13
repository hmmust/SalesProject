
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="homepage"),
    path("add/", views.ProductAdd.as_view(), name="add"),
    path("delete/<int:pk>", views.ProductDelete.as_view(), name="delete"),
    path("update/<int:pk>", views.ProductUpdate.as_view(), name="update"),

]
