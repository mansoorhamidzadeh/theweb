from django.urls import path
from rest_framework import routers
from . import views


urlpatterns=[
    path('api-list/',views.getRoutes),
    path('',views.CustomerApiView.as_view())
]