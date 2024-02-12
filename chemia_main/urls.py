from django.urls import path, include

from . import views

app_name = 'chemia_main'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    
]
