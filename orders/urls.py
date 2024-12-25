from django.urls import path
from orders import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order_history/', views.order_history, name='order_history')
]