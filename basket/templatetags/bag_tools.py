from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_discount_subtotal')
def calc_discount_subtotal(discounted_price, quantity):
    return discounted_price * quantity
