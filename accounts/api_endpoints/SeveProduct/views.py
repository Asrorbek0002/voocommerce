from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from products.models import Product
from accounts.api_endpoints.SeveProduct.serializers import SaveProductSerializer


class SaveProductAPIView(APIView):
    queryset = Product.objects.all()
    permission_classes = SaveProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=SaveProductSerializer)
    def post(self, request, *args, **kwargs):
        if request.data.get("id"):
            product = get_object_or_404(Product, id = request.data["id"])

            if product in self.request.user.saved_products.all():
                self.request.user.save_products.remove(product)
            else:
                self.request.user.saved_products.add(product)

            return Response({"detail": "Sccess"}, status=400)

        return Response({"detail": "Product id is required."}, status=400)

















