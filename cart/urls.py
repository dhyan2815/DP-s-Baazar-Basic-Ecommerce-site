from django.urls import path
from cart import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]