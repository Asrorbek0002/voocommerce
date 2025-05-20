from rest_framework.generics import CreateAPIView
from products.models import Category
from products.api_endpoints.CategoryCreate.serializers import CategoryCreateSerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)



