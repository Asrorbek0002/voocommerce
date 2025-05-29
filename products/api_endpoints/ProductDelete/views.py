from rest_framework.generics import GenericAPIView

from products.models import Product

class ProductDeleteAPIView(GenericAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


__all__ = ["ProductDeleteAPIView"]




















