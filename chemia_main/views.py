from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse

from .models import Product, Category 

def index(request):
    return render(request, 'chemia_main/index.html')

def products(request):
    products = get_list_or_404(Product)
    return render(request, 'chemia_main/products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'chemia_main/product_detail.html', {
        'product_id': product_id,
        'product': product,
        })

def about(request):
    return render(request, 'chemia_main/about.html')

