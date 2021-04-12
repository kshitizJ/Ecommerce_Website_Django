# importing render, JsonResponse and all the model classes from models.py
# render function sends the request to the html page which renders out the content on web browser
# JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response. Its default Content-Type header is set to application/json. If the safe parameter is set to False , any object can be passed for serialization; otherwise only dict instances are allowed.
# .models is the python file where we have all our model classes. We are importing all the classes using '*' symbol to use those classes in our views.py

from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, guestOrder

# Create your views here.


# store function is responsible for rendering store.html where we can see all the products
def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}

    # here we return the render function
    return render(request, 'templates/store/Store.html', context)


# cart function is responsible for rendering cart.html where we check if the user is authenticated or not, if user is authenticated then show the cart else the cart will be empty
def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'templates/store/Cart.html', context)


# checkout funtion is responsible for rendering checkout.html where we first if the user is authenticated or not, if authenticated then show the total items and total bill.
def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'templates/store/Checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    # In this function if we define a list of dictionaries we set "safe" to False. If we did not set this parameter, we would get a TypeError with the following message:
    # "In order to allow non-dict objects to be serialized set the safe parameter to False."
    # By default, JsonResponse accepts only Python dictionaries.
    return JsonResponse('Item was added.', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)
