from django.shortcuts import render
from django.http import HttpResponse
from catalogue.models import Product


 
def products(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'catalogue/products.html', context)
    
