
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "products"
urlpatterns = [
    path("", login_required( views.ProductList.as_view(), login_url="accounts:login" ), name="homepage"),
    path("add/",login_required( views.ProductAdd.as_view() , login_url="accounts:login" ), name="add"),
    path("delete/<int:pk>", views.ProductDelete.as_view(), name="delete"),
    path("update/<int:pk>", views.ProductUpdate.as_view(), name="update"),

]
