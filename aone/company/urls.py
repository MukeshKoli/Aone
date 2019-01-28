from django.urls import path
from . import views

app_name = "company"

urlpatterns = [

    path('', views.ListCompany.as_view(), name="listCompany"),
    path('create/', views.CreateCompany.as_view(), name="createCompany"),
    path('update/<int:pk>/', views.UpdateCompany.as_view(), name="updateCompany"),
    path('delete/<int:pk>/', views.DeleteCompany.as_view(), name="deleteCompany"),


]

