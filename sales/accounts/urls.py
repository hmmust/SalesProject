
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.AccountLogin.as_view(), name="login"),
    path("logout/", views.AccountLogout.as_view(), name="logout"),

    #   path("delete/<int:pk>", views.ProductDelete.as_view(), name="delete"),
 #   path("update/<int:pk>", views.ProductUpdate.as_view(), name="update"),

]
