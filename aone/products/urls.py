from django.urls import path
from . import views

app_name = "products"

urlpatterns = [

    path('', views.ListProducts.as_view(), name="listProd"),
    path('create/', views.CreateProducts.as_view(), name="createProd")

]



