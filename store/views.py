from ctypes import HRESULT
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(request):
    return render(request, 'home.html', )

def store(request):
    products= Product.objects.all()
    return render(request, 'store.html', {'products': products})