from django.core.serializers import serialize
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from products.models import Size
from products.api_endpoints.SizeList.serializers import SizeListSerializer

class SizeListAPIView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)


class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, reqest, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)


















