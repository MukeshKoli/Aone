from django.urls import path, include
from . import views

app_name = "bills"

urlpatterns = [

    path('', views.ListBills.as_view(), name="listBills"),
    path('create/', views.CreateBills.as_view(), name="createBills"),
    path('select2/', include('django_select2.urls')),
]
