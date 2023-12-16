from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from django.conf import settings
import os
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Product

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

# вот сюда почему-то не попадает - почему?

@require_POST
def buy(request, product_id):
    print('Смотрим здесь')
    # Логика покупки товара
    product = get_product_by_id(product_id)
    
    # Логика работы с Stripe...
    
    messages.success(request, f'Вы успешно купили товар: {product.name}. Спасибо за покупку!')
    # return redirect('success')  # Замените 'success' на имя вашей страницы успешной покупки
    return redirect('index')

def get_product_by_id(product_id):
    # Получение товара по его идентификатору
    print('До этого момента все хорошо')
    product = get_object_or_404(Product, id=product_id)
    return product