from django.urls import path

from products.api_endpoints import *

urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name = "product-list")
]














