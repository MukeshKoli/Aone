from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from bills.models import Bills
from company.models import Company
from .forms import BillsForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ListBills(generic.ListView):

    model = Bills
    context_object_name = "billsList"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        comp_id = Bills.objects.values_list('compName', flat=True).distinct()
        comp_name_id =[]
        for ore in comp_id:

            name_list = Company.objects.get(pk=ore)
            comp_name_id.append(name_list)

        context['comp_name_list'] = set(comp_name_id)
        return context



class CreateBills(LoginRequiredMixin, generic.CreateView):

    model = Bills
    form_class = BillsForm
    success_url = reverse_lazy("bills:listBills")







