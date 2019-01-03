from django.shortcuts import render
from django.views import generic
from accounts import forms
from django.urls import reverse_lazy


class SignUp(generic.CreateView):

    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"



