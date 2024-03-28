from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse

from .models import Product, Category 

def index(request):
    language = request.GET.get('lang', 'en')
    belts_id = Category.objects.get(name='Leather Belt').id
    bags_id = Category.objects.get(name='Leather Bag').id
    wallet_id = Category.objects.get(name='Leather Wallet').id
    return render(request, 'chemia_main/index.html', {'language': language,
                                                      'belts': belts_id,
                                                      'bags': bags_id,
                                                      'wallets': wallet_id,})

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

def products_by_category(request, category_id):
    language = request.GET.get('lang', 'en')
    products = get_list_or_404(Product, category=category_id)
    categories = get_list_or_404(Category)

    return render(request, 'chemia_main/products.html', {'products': products,
                                                         'language': language,
                                                         'categories': categories,
                                                         })

def about(request):
    language = request.GET.get('lang', 'en')
    return render(request, 'chemia_main/about.html', {
        'language': language,
    })

