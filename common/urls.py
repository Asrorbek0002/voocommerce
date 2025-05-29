from django.urls import path

from common.api_endpoints import *
from common.views import HomeView, ContactView, ShoppingCartView

app_name = "common"

urlpatterns = [
    path("media/upload/", MediaFileCreateAPIView.as_view(), name = "media-upload"),
    path("media/delete/<int:id>/", MediaFileDestroyAPIView.as_view(), name = "media-delete"),

    path("index/", HomeView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name = "contact"),
    path("cart/", ShoppingCartView.as_view(), name = "shopping-cart")
]




