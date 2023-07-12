from django.shortcuts import render
from .models import Product


# Inspired by Ado Boutique
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    print(products)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)