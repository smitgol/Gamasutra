from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name="Home"),
    path('<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
    path('Games By Size', views.ProductListView_card.as_view(), name="card"),
    path('Games By Company', views.ProductListView_card1.as_view(), name="card1"),
    path('Games By Type', views.ProductListView_card2.as_view(), name="card2"),
    path('About us', views.About_us, name="Aboutus"),
    path('Websites', views.website, name="website")
]
