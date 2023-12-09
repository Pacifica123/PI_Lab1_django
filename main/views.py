from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products, 'media_root': settings.MEDIA_ROOT, 'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'main/index.html', context=context)

def serve_image(request, image_path):
    image_path = os.path.join(settings.MEDIA_ROOT, image_path)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img:
            return HttpResponse(img.read(), content_type="image/jpeg")  # Уточни тип содержимого в соответствии с расширением файла
    return HttpResponse(status=404)