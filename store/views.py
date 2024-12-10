from django.shortcuts import render,get_object_or_404

from .models import Category,Product

# Create your views here.

def categories(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }


def products_all(request):

    products = Product.products.all()
    

    return render(request, 'store/store.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    print(product)
    return render(request, 'store/products/single.html', {'product': product})


def category_list(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)
    print(category)
    products = Product.products.filter(category=category)
    print(products)

    return render(request, 'store/products/categroy.html', {'category': category, 'products': products})

