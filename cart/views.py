from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    request.session['cart_id'] = cart.id
    items = cart.items.all()
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'items': items})

@login_required
def profile(request):
    cart, _ = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    cart_items = cart.items.all()
    context = {
        'user' : request.user,
        'cart_items' : cart_items,
    }
    return render(request, 'cart/profile.html', context)

def add_to_cart(request, product_id):
    cart, _ = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    request.session['cart_id'] = cart.id
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')