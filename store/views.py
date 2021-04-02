from django.shortcuts import render
from .models import *
# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'templates/store/Store.html', context)


def cart(request):
    context = {}
    return render(request, 'templates/store/Cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'templates/store/Checkout.html', context)
