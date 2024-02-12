from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'chemia_main/index.html')

def products(request):
    return render(request, 'chemia_main/products.html')

def product_detail(request, product_id):
    return render(request, 'chemia_main/product_detail.html', {'product_id': product_id})

def about(request):
    return render(request, 'chemia_main/about.html')

