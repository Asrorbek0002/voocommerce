from django.urls import path

from accounts.api_endpoints import *


urlpatterns = [
    path('login/', SesssionLoginAPIView.as_view(), name = 'account-login'),
    path('logout/', SessionLogoutAPIView.as_view(), name = 'account-logaut')
]




