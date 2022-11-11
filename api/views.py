from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from customer.models import Customer
from .serializers import CustomerSerializer


class CustomerApiView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
