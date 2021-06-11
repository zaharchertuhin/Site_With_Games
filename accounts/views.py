from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import Login
from django.urls import reverse_lazy

class UserCreationView(CreateView):
    form_class = Login
    success_url = reverse_lazy("login")
    template_name = "accounts/sign_up.html"