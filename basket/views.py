from django.shortcuts import (render, redirect, reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ This view renders the basket content """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add the specified quantity of products to the basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'You have now {basket[item_id]} \
                         {product.name}s in your basket')
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

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'You have now {basket[item_id]} \
                         {product.name} in your basket')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Removes an item from the basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
