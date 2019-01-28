from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from . import models
from products.models import Products
from company.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ListProducts(generic.ListView):

    model = Products
    context_object_name = "productsList"
    # This "context_object_name" will be used to iterate for list view.

    def get_context_data(self, **kwargs):
        """
        This will pass the values into the dropdown
        Products and Order has the Foreign key to compName of Company.
        Fetched the id from Products and used to get the values from Company model
        and used set for distinct values.
        """
        context = super().get_context_data(**kwargs)
        comp_id = Products.objects.values_list('compName', flat=True).distinct()
        comp_name_id = []
        for ore in comp_id:

            name_list = Company.objects.get(pk=ore)
            comp_name_id.append(name_list)

        context['comp_name_list'] = set(comp_name_id)
        return context



class CreateProducts(LoginRequiredMixin, generic.CreateView):

    model = Products
    fields = "__all__"
    success_url = reverse_lazy("products:listProd")


class UpdateProducts(LoginRequiredMixin, generic.UpdateView):

  model = Products
  fields = "__all__"
  template_name_suffix = "_update_form"
  success_url = reverse_lazy("products:listProd")


class DeleteProducts(LoginRequiredMixin, generic.DeleteView):

    model = Products
    success_url = reverse_lazy("products:listProd")