from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from orders.models import Orders
from .forms import OrderForm
from products.models import Products

# Create your views here.


class ListOrders(generic.ListView):

    model = Orders
    context_object_name = "ordersList"


class CreateOrders(generic.CreateView):

    model = Orders
    # Order Id will be generated when form is saved.
    form_class = OrderForm
    success_url = reverse_lazy("orders:listOrders")


def load_items(request):

    compName_id = request.GET.get('compName')
    items = Products.objects.filter(compName_id=compName_id).order_by('compName')
    return render(request, "orders/items_dropdown_list.html", {'items': items})


