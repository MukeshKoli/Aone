from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [

    path('', views.ListOrders.as_view(), name="listOrders"),
    path('create/', views.CreateOrders.as_view(), name="createOrders"),
    path('ajax/load-items/', views.load_items, name="ajax_load_items"),
<<<<<<< HEAD
    path('update/<int:pk>/', views.UpdateOrders.as_view(), name="updateOrders"),
    path('delete/<int:pk>/', views.DeleteOrders.as_view(), name="deleteOrders")
=======
>>>>>>> b485e7c327aed112c5b759b728aabce054f19b09

]
