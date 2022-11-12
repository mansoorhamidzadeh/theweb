from django.urls import path
from . import views
urlpatterns=[
    path('',views.customer,name='customer'),
    path('customerclick/',views.customerclick_view,name='customerclick'),
    path('customersignup/', views.customer_signup_view,name='customersignup'),
]