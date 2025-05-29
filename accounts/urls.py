from django.urls import path

from accounts.api_endpoints import SessionLogoutAPIView, SesssionLoginAPIView, CartItemListAPIView, CartItemsCreateAPIView, CartItemUpdateAPIView, CartitemDeleteAPIView


urlpatterns = [
    path('login/', SesssionLoginAPIView.as_view(), name = 'account-login'),
    path('logout/', SessionLogoutAPIView.as_view(), name = 'account-logaut'),
    path('cart/', CartItemListAPIView.as_view() , name = "cart-items"),
    path('cart/cartitems/create/', CartItemsCreateAPIView.as_view(), name = "cart-items-create"),
    path('cart/cartitems/<int:pk>/update/', CartItemUpdateAPIView.as_view(), name = "cart-items-update"),
    path('cart/cartitems/<int:pk>/delete/', CartitemDeleteAPIView.as_view(), name = "cart-item-delete")

]




