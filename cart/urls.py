from django.urls import path
from .views import cart_home, cart_update

urlpatterns = [
    path('', cart_home, name="cart_home"),
    path('update/', cart_update, name="cart_add")
]