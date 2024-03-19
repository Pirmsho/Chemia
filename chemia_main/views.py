from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse

from .models import Product, Category 

def index(request):
    language = request.GET.get('lang', 'en')
    return render(request, 'chemia_main/index.html', {'language': language})

def products(request):
    language = request.GET.get('lang', 'en')
    products = get_list_or_404(Product)
    categories = get_list_or_404(Category)
    return render(request, 'chemia_main/products.html', {'products': products,
                                                         'language': language,
                                                         'categories': categories,})

def product_detail(request, product_id):
    language = request.GET.get('lang', 'en')
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'chemia_main/product_detail.html', {
        'product_id': product_id,
        'product': product,
        'language': language,
        })

def about(request):
    language = request.GET.get('lang', 'en')
    return render(request, 'chemia_main/about.html', {
        'language': language,
    })

