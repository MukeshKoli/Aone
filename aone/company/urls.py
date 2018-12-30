from django.urls import path
from . import views

app_name = "company"

urlpatterns = [

    path('', views.ListCompany.as_view(), name="listCompany"),
    path('create/', views.CreateCompany.as_view(), name="createCompany")

]

