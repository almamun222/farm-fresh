from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product, Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
# Create your views here.

def product(request):
    data = Product.objects.all()
    return render(request, 'product.html', {'data': data})



def curt(request):
    return render(request, 'curt.html')

def checkout(request):
    return render(request, 'checkout.html')

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Order, OrderItem

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'User not authenticated'}, status=401)

        data = json.loads(request.body)
        title = data.get("name")
        quantity = int(data.get("quantity", 1))

        try:
            product = Product.objects.get(title=title)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def submit_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order = Order.objects.create(
            customer_name=data['name'],
            phone=data['phone'],
            address=data['address'],
            payment_method=data['payment']
        )
        for item in data['cart']:
            OrderItem.objects.create(
                order=order,
                product_name=item['name'],
                price=item['price'],
                quantity=item['quantity']
            )
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid method"}, status=400)


