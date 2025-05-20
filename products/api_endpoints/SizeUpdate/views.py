from rest_framework.generics import UpdateAPIView
from products.models import Size
from products.api_endpoints.SizeUpdate.serializers import SizeUpdateSerializer

class SizeUpdateAPIView(UpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeUpdateSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


