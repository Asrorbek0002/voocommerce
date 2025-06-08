from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Cart, User


@receiver(post_save, sender = User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user = instance)



@receiver(post_delete, sender = User)
def delete_cart(sender, instance, **kwargs):
    instance.cart.delete()














