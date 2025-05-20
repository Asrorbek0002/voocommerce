from rest_framework.generics import DestroyAPIView
from products.models import Color
from products.api_endpoints.ColorDelete.serializers import ColorDeleteSerializer


class ColorDeleteAPIView(DestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorDeleteSerializer

    def delete(self, request, *args, **kwargs):
        return self.serializer_class(request, *args, **kwargs)