from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ This view renders the basket content """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add the specified quantity of products to the basket """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        if quantity == 1:
            messages.success(request, f'The {product.name} is in your basket')
        else:
            messages.success(
                request, f'The {quantity} {product.name}s are in your basket'
                 )

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust quantity and amount of a specified product"""

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Removes an item from the basket"""

    try:
        basket = request.session.get('basket', {})
        print()
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
