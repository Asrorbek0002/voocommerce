from rest_framework.generics import UpdateAPIView
from products.models import Category
from products.api_endpoints.CategoryUpdate.serializers import CategoryUpdateSerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
