from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from bills.models import Bills

# Create your views here.


class ListBills(generic.ListView):

    model = Bills
    context_object_name = "billsList"


class CreateBills(generic.CreateView):

    model = Bills
    fields = ('compName', 'orderId', 'createdBy', 'billAmount', 'billStatus')
    success_url = reverse_lazy("bills:listBills")



