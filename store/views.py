from ctypes import HRESULT
from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.mail import send_mail   

def home(request):
    return render(request, 'home.html')

def products(request):
    queryset = Product.objects.all()
    return render(request, 'products.html', {"products":queryset})

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def promotions(request):
    return render(request, 'promotions.html')