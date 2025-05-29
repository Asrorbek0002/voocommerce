from django.utils.text import slugify
from  rest_framework import serializers

from products.models import Category, Product


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "brand", "default_images", "category"]


    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.description,
            "brand": instance.brand,
            "default_images": instance.default_images,
            "slug": instance.slug,
            "is_active": instance.is_active,
            "category": CategoryCreateSerializer(instance.category).data

        }

        return instance

    def create(self, validated_data):
        is_exists = Product.objects.filter(slug=slugify(validated_data["name"])).exists()
        if is_exists:
            return serializers.ValidationError("Product with this name already exists (or deactivated).")

        return Product.objects.create(
            slug = slugify(validated_data["name"]),
            **validated_data
        )












