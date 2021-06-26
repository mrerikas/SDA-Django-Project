from django.shortcuts import render
from .models import *


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/shop.html', context)


def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)
