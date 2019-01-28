from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from orders.models import Orders
from .forms import OrderForm
from products.models import Products
<<<<<<< HEAD
from company.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
=======
>>>>>>> b485e7c327aed112c5b759b728aabce054f19b09

# Create your views here.


class ListOrders(generic.ListView):

    model = Orders
    context_object_name = "ordersList"

    def get_context_data(self, **kwargs):
        """
        This will pass the values into the dropdown filter on the top.
        Products and Order has the Foreign key to compName of Company.
        Fetched the id from Products and used to get the values from Company model
        and used set for distinct values.
        """
        context = super().get_context_data(**kwargs)
        comp_id = Orders.objects.values_list('compName', flat=True).distinct()
        comp_name_id = []
        for ore in comp_id:

            name_list = Company.objects.get(pk=ore)
            comp_name_id.append(name_list)

        context['comp_name_list'] = set(comp_name_id)
        return context


class CreateOrders(LoginRequiredMixin, generic.CreateView):

    model = Orders
    # Order Id will be generated when form is saved.
    form_class = OrderForm
    success_url = reverse_lazy("orders:listOrders")


def load_items(request):

    compName_id = request.GET.get('compName')
    items = Products.objects.filter(compName_id=compName_id).order_by('compName')
    return render(request, "orders/items_dropdown_list.html", {'items': items})


class UpdateOrders(LoginRequiredMixin, generic.UpdateView):

    model = Orders
    form_class = OrderForm
    success_url = reverse_lazy("orders:listOrders")

class DeleteOrders(LoginRequiredMixin, generic.DeleteView):

    model = Orders
    success_url = reverse_lazy("orders:listOrders")
