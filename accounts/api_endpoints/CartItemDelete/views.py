from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions

from accounts.models import CartItem
from accounts.api_endpoints.CartItemDelete.serializers import CartitemDeleteSerializer


class CartitemDeleteAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartitemDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]


    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


    def delete_cart(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(owner = self.request.user)








