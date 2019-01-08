from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [

    path('', views.ListOrders.as_view(), name="listOrders"),
    path('create/', views.CreateOrders.as_view(), name="createOrders"),
    path('ajax/load-items/', views.load_items, name="ajax_load_items"),

]
