from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})