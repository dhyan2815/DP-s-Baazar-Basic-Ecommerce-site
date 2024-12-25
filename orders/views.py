from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from orders.models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_order(request):
    cart_id = request.session.get('cart_id') #this will create a user-centric session of cart_id when creating an order
    cart = Cart.objects.get(id=cart_id) #fetches cart id from Cart's object which stores in the database
    if request.method == 'POST':
        order = Order.objects.create(
            customer_name = request.POST.get('name'),
            email = request.POST.get('email'),
            address = request.POST.get('address')
        )
    
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity = item.quantity,
                price = item.product.price
            )
        CartItem.objects.all().delete() #clears cart after ordering
        return redirect('order_confirmation')
    return render(request, 'orders/create_order.html', {'cart':cart})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def order_confirmation(request):
    return render(request, 'orders/order_confirmation.html')