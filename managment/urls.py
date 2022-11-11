
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('insurance.urls')),
    path('customer/',include('customer.urls')),
    path('api/',include('api.urls')),
]
