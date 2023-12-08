from django.urls import path
from .views import checkout, charge
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('charge/', charge, name='charge'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)