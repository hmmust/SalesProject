from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView



# Create your views here.
class AccountLogin(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("products:homepage")


class AccountLogout(LogoutView):
    http_method_names = ["get","post"]
    next_page = reverse_lazy("accounts:login")

    def get(self ,request):
        return super().post(request)

