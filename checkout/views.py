from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NO3ChF76CufBdvKkJTW1jz01g98EPHMQ0kAGAwc33wdUd00p6ENtleKvlJeMcAojKGLwew18TSnoFPt6czl6Ggn00T2kI76nF',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
