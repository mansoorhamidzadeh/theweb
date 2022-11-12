from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from customer.models import Customer
from .serializers import CustomerSerializer
from django.http import JsonResponse



def getRoutes(request):
    routes=[
        {'GET':"/api/"}
    ]
    return JsonResponse(routes,safe=False)
class CustomerApiView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
