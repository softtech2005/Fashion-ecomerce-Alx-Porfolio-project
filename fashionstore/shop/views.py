from django.shortcuts import render

# Create your views here.
from.models import Product

def home(request):
    return render(request, 'shop/index')

def shop(request):
    Products = Product.objects.all()
    return render(request, 'shop/shop.html', {'Products':Products})

def product_details(request, product_id):
    product = product.objects.get(id=product_id)