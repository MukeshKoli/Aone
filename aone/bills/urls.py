from django.urls import path
from . import views

app_name = "bills"

urlpatterns = [

    path('', views.ListBills.as_view(), name="listBills"),
    path('create/', views.CreateBills.as_view(), name="createBills")
]
