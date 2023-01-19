from django.urls import path

from app.views import (
    CustomerList, CustomerDetail, InsuranceList, InsuranceDetail, ProductList, ProductDetail)

urlpatterns = [
    path("products/", ProductList.as_view(), name="products-list"),
    path("products/<str:pk>/", ProductDetail.as_view(), name="products-detail"),
    path("customers/", CustomerList.as_view(), name="customers-list"),
    path("customers/<str:pk>/", CustomerDetail.as_view(), name="customers-detail"),
    path("insurance/", InsuranceList.as_view(), name="insurances-list"),
    path("insurance/<str:pk>/", InsuranceDetail.as_view(), name="insurances-detail"),
]