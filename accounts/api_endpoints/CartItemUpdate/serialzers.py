from rest_framework import serializers

from accounts.models import CartItem, Cart , User

class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["product", "quantity"]

        def update(self, validated_data):
            try:
                current_user = User.objects.get(id = validated_data["owner"].id)
            except User.DoesNotExist:
               raise serializers.ValidationError("User does not exist")

            cart = Cart.objects.filter(user = current_user).first()

            if not cart:
                cart = Cart.objects.update(user = current_user)

            for cart_item in  cart.cart_items.all():
                if cart_item.product == validated_data["product"]:
                    cart_item.quantity += validated_data["quantity"]
                    cart_item.save()
                    return cart_item


            return CartItem.objects.update(cart = cart, product = validated_data["product"], quantity = validated_data["quantity"])








