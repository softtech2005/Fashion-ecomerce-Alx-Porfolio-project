from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request, 'shop/index.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product.html', {'product': product})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')
