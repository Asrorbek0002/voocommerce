from django.urls import path

from products.api_endpoints import *
from products.api_endpoints.CategoryCreate.views import CategoryCreateAPIView
from products.api_endpoints.CategoryDelete.views import CategoryDeleteAPIView
from products.api_endpoints.CategoryUpdate.views import CategoryUpdateAPIView

urlpatterns = [

    path('list1/', ProductListAPIView1.as_view(), name = "product-list"),
    path('list2/', ProductListAPIView2.as_view(), name = "product-list2"),
    path('list3/', ProductListView3.as_view(), name = "product-list3"),

    path('categories/',CategoryListView.as_view(), name = "category-list" ),
    path('categories/create/', CategoryCreateAPIView.as_view(), name = "category-create"),
    path('categories/<str:slug>/', CategoryRetrieveAPIView.as_view(), name = "category-retrieve"),
    path('categories/<str:slug>/update/', CategoryUpdateAPIView.as_view(), name = "category-update"),
    path('categories/<str:slug>/delete/', CategoryDeleteAPIView.as_view(), name = "category-delete")
]














