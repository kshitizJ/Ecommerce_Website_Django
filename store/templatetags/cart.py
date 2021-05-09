from django import template

register = template.Library() #all tags and filters are registered here


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

#to display the total price of a product
@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)

#to display the sum total of the orders
@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)

    return sum

