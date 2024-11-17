from django.shortcuts import render
from catalogue.models import Product

def index(request):
    context = {}
    products = Product.objects.all()[:8]
    context['products'] = products
    return render(request, 'main/index.html', context)