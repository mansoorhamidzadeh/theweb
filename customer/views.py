from django.shortcuts import render,HttpResponse

# Create your views here.

def customer(request):
    return HttpResponse('this is from customers')
