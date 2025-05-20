from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from products.models import Color
from products.api_endpoints.ColorCreate.serializers import ColorCreateSerializer

class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorCreateSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, *kwargs)





