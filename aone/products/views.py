from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from . import models
from products.models import Products


# Create your views here.

class ListProducts(generic.ListView):

    context_object_name = "productsList"
    # This "context_object_name" will be used to iterate for list view.

    model = Products


class CreateProducts(generic.CreateView):

    model = Products
    fields = "__all__"
    success_url = reverse_lazy("products:listProd")

