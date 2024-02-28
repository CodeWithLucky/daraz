from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Product

# Create your views here.
class ProductView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'prod'
    pk_url_kwarg = 'sku'