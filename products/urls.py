from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search_products, name='search'),
]