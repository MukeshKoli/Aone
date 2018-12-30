from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from orders.models import Orders


# Create your views here.

class ListOrders(generic.ListView):

    model = Orders
    context_object_name = "ordersList"


class CreateOrders(generic.CreateView):

    model = Orders
    fields = ('orderId', 'orderDate', 'compName', 'itemName', 'orderStatus')
    success_url = reverse_lazy("orders:listOrders")


