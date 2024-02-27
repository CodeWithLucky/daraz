from django.urls import path
from . views import ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('<str:sku>/', ProductDetailView.as_view(), name='product-detail'),
]
