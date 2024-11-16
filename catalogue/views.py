from django.shortcuts import render
from django.http import HttpResponse
from catalogue.models import Product


def products(requests):
    products = Product.objects.all()
    product_list = []
    for product in products:
        product_list.append(product.title)
    return HttpResponse(f"Products: {product_list} ")
