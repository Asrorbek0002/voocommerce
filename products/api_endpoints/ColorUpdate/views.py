from rest_framework.generics import UpdateAPIView
from products.models import Color
from products.api_endpoints.ColorUpdate.serializers import ColorUpdateSerializer

class ColorUpdataAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorUpdateSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, *kwargs)
