from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.contrib.auth.models import User
from products.models import Product


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        filter_kwargs = {'id': cart_id}
        if request.user.is_authenticated:
            filter_kwargs.update({'user': request.user})

        cart_obj, created = Cart.objects.get_or_create(**filter_kwargs)

        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
        request.session['cart_id'] = cart_obj.id
        return cart_obj, created

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def pre_save_cart_recevier(sender, instance, action, *args, **kwargs):
    print(instance.products.all())
    print(action)
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        instance.save()


m2m_changed.connect(pre_save_cart_recevier, sender=Cart.products.through)
