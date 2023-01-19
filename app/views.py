from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from app.serializer import ( InsuranceSerializer, ProductSerializer, CustomerSerializer)

from .models import (
    Product, Customer, Insurance
)


class ProductList(ListCreateAPIView):
    """
    List all products or create a new product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a product instance.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerList(ListCreateAPIView):
    """
    List all customers or create a new customer.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a customer instance.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class InsuranceList(ListCreateAPIView):
    """
    List all insurances or create a new insurance.
    """

    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

class InsuranceDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a insurance instance.
    """

    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
