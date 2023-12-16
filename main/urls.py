from django.urls import path
from .views import index, serve_image, buy

urlpatterns = [
    path('index/', index, name='index'),
    path('media/photos/<str:image_path>/', serve_image, name='serve_image'),
    path('buy/<int:product_id>/', buy, name='buy')
]