from django.shortcuts import render,HttpResponse
from customer.models import  Customer
# Create your views here.



def home_view(request):
    return render(request,'insurance/adminbase.html')
def admin_view_customer_view(request):
    customers=Customer.objects.all()
    context={'customers':customers}
    return render(request,'insurance/admin_view_customer.html',context)