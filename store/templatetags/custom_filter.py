from django import template

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)


@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1


@register.filter(name='total_in_bill')
def total_in_bill(orders):
    sum = 0
    for order in orders:
        sum += multiply(order.quantity, order.price)
    return sum
