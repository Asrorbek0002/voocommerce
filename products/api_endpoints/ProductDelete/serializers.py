from rest_framework import serializers
from django.utils.text import slugify

from products.models import Category, Product


class CategoryDeleteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "brand", "default_images", "category"]

    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "brand": instance.brand,
            "default_images": instance.default_images,
            "slug": instance.slug,
            "is_active": instance.is_active,
            "category": CategoryDeleteSerilizer(instance.category).data

        }
        return instance

    def delete(self, valiated_data):
        is_exists = Product.objects.filter(slug = slugify(valiated_data["name"])).exists()
        if is_exists:
            return serializers.ValidationError("Product with this name already exists or (deactivated).")

        return Product.objects.delete(
            slug = slugify(valiated_data["name"]), **valiated_data
        )






