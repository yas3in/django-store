from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product, ProductImage
from apps.basket.forms import AddToBasketForm

 
def products(request):
    context = {}
    products = Product.objects.all()
    products_images = ProductImage.objects.all()
    context['products'] = products
    context['products_images'] = products_images
    return render(request, 'catalogue/products.html', context)
    
    
def product_detail(request, id):
    queryset = Product.objects.filter(is_active=True).filter(id=id)
    if queryset.exists():
        product = queryset.first()
        form = AddToBasketForm({"product": product.id, 'quantity': 1})
        return render(request, 'catalogue/product_detail.html', {'product': product, 'form': form})
    raise Http404
