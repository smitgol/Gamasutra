from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()

    cart_obj.save()
    return render(request, "home.html", {'cart': cart_obj})

@login_required
def cart_update(request):
    product_id = request.POST.get('product_id')
    try:
        product_obj = Product.objects.get(pk=product_id)
    except ObjectDoesNotExist:
        return redirect('cart_home')
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
        messages.success(request, "Game successfully removed from wishlist")
    else:
        cart_obj.products.add(product_obj)
        messages.success(request, "Game successfully added to wishlist")

    return redirect('cart_home')
