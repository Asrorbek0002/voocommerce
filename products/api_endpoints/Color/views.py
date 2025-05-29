from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from products.models import Color
from rest_framework import permissions
from products.api_endpoints.Color.serializers import ColorSerializer

class ColorListCreateView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ColorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]