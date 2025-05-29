from django.core.serializers import serialize
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework.response import  Response

from accounts.api_endpoints.CartItemList.serializers import CartItemSerializer
from accounts.models import CartItem


class CartItemListAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = []

    def get(self,request, *args, **kwargs):
        serializer = CartItemSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)



