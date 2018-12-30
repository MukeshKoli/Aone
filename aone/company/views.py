from django.shortcuts import render
from django.views import generic
from company.models import Company
from django.urls import reverse, reverse_lazy
from . import models

# Create your views here.


class ListCompany(generic.ListView):
    model = Company


class CreateCompany(generic.CreateView):

    model = Company
    fields = "__all__"
    success_url = reverse_lazy('company:listCompany')
