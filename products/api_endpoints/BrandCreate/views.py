from rest_framework.generics import CreateAPIView
from products.api_endpoints.BrandCreate.serializers import BrandCreateSerializer
from products.models import Brand


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)




