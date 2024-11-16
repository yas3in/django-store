from django.shortcuts import render
from django.http import HttpResponse
from catalogue.models import Product


 
def products(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'catalogue/products.html', context)
    
def product_detail(request, id):
    context = {}
    products = Product.objects.filter(id=id)
    context['products'] = products
    return render(request, 'catalogue/product_detail.html', context)
