from rest_framework.generics import DestroyAPIView
from products.api_endpoints.BrandDelete.serializers import BrandDeleteSerializer
from products.models import Brand

class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDeleteSerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)