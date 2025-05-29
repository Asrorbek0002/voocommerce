from django.template.defaultfilters import slugify
from  rest_framework import serializers

from products.models import Product, Category

class CategoryProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", 'brand', "default_images", "category"]



    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "brand": instance.brand,
            "slug": instance.slug,
            "is_active": instance.is_activate,
            "category": CategoryProductUpdateSerializer(instance.category).data

              }
        return instance

    def update(self, instance, validated_data):
        if "name" in validated_data:
            validated_data["slug"] = slugify(validated_data["name"])
        return super().update(instance, validated_data)









