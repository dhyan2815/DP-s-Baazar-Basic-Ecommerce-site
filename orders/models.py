from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #adds field when the object is first created
    updated_at = models.DateTimeField(auto_now=True) #adds to the current field when the object is saved

def __str__(self):
    return f"Order {self.id} for {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)

def __str__(self):
    return f"{self.product.name} x{self.quantity}"