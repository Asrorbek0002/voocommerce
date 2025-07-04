from django.urls import path

from common.api_endpoints import *
from common.views import HomeView, ContactView, ShoppingCartView, ProfileView

app_name = "common"

urlpatterns = [
    path("media/upload/", MediaFileCreateAPIView.as_view(), name = "media-upload"),
    path("media/delete/<int:id>/", MediaFileDestroyAPIView.as_view(), name = "media-delete"),

    path("", HomeView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name = "contact"),
    path("cart/", ShoppingCartView.as_view(), name = "shopping-cart"),
    path('profile/', ProfileView.as_view(), name = "profile")

]




