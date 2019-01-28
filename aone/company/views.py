from django.shortcuts import render
from django.views import generic
from company.models import Company
from django.urls import reverse, reverse_lazy
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ListCompany(generic.ListView):

    model = Company


class CreateCompany(LoginRequiredMixin, generic.CreateView):

    model = Company
    fields = "__all__"
    success_url = reverse_lazy('company:listCompany')


class UpdateCompany(LoginRequiredMixin, generic.UpdateView):

    model = Company
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('company:listCompany')


class DeleteCompany(LoginRequiredMixin, generic.DeleteView):

    model = Company
    success_url = reverse_lazy('company:listCompany')
