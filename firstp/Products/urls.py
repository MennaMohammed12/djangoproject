from django.urls import path
from Products.views import index

urlpatterns=[
    path('index',index),
]