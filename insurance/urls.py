from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_view,name='home-view'),
    path('admin-view-customer',views.admin_view_customer_view,name='admin-view-customer')
]