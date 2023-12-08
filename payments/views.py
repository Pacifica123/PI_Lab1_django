from django.shortcuts import render
from django.http import JsonResponse
import stripe
from django.conf import settings
from djstripe.models import Product

stripe.api_key = settings.SECRET_KEY

def checkout(request):
    products = Product.objects.all() # здесь будет способ получения товаров
    return render(request, 'payments/checkout.html', {'products': products})

def charge(request):
    if request.method == 'POST':
        # Логика обработки платежа с использованием Stripe API
        try:
            charge = stripe.Charge.create(
                amount=2000,  # Сумма в центах
                # currency='usd',
                description='Описание платежа',
                source=request.POST['stripeToken']
            )
            return JsonResponse({'message': 'Payment successful!'})
        except stripe.error.CardError as e:
            return JsonResponse({'error': str(e)})
