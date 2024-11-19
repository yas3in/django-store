from django.shortcuts import render
from django.http import HttpResponse
from catalogue.models import Product, ProductImage
from basket.forms import AddToBasketForm

 
def products(request):
    context = {}
    products = Product.objects.all()
    products_images = ProductImage.objects.all()
    context['products'] = products
    context['products_images'] = products_images
    return render(request, 'catalogue/products.html', context)
    
def product_detail(request, id):
    context = {}
    products = Product.objects.filter(id=id)
    form = AddToBasketForm({"product": products, 'quantity': 1})
    context['products'] = products
    context['form'] = form
    return render(request, 'catalogue/product_detail.html', context)
