from rest_framework.generics import UpdateAPIView
from products.api_endpoints.BrandUpdate.serializers import BrandUpdateSerializer
from products.models import Brand

class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)










