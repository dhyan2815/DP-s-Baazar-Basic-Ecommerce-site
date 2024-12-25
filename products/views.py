from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.db.models import Q

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {"products" : products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def search_products(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'products/search_results.html', {'query': query, 'results': results})