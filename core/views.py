from django.shortcuts import  render
from store.models import Product


def index(request):

    products = Product.products.all()

    return  render(request,'core/index.html',{'products': products[2:]})