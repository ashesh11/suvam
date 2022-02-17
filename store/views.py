from ctypes import HRESULT
from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product

def hello(request):

    query_set = Product.objects.all()

    return render(request, 'store.html', {'products': query_set})
