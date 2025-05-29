from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework.mixins import UpdateModelMixin

from products.models import Product
from products.api_endpoints.ProductUpdate.serializers import ProductUpdateSerializer

class ProductUpdateAPIView(GenericAPIView, UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


__all__ = ["ProductUpdateAPIView"]