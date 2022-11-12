from django.shortcuts import render,HttpResponse
from .form import *
# Create your views here.

def customer(request):

    return render(request,'customer/index.html',{"fggfg":"gfgfgf"})

def customerclick_view(request):
    return render(request,'customer/customerclick.html')

def customer_signup_view(request):
    userForm=CustomerUserForm()
    customerForm=CustomerForm()
    if request.method=='POST':
        userForm=CustomerUserForm(request.POST)
        customerForm=CustomerForm(request.POST)
        if userForm.is_valid() and customerForm.is_valid():
            print(request.POST)

    mydict={'userForm':userForm,'customerForm':customerForm}


    return render(request,'customer/customersignup.html',mydict)
