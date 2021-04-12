# django automatically import admin module in the store app because django.contrib.admin is added in our setting.py. This function attempts to import an admin module in each installed application. Such modules are expected to register models with the admin.
# .models is the python file where we have all our model classes. We are importing all the classes using '*' symbol to register those classes in our admin panel

from django.contrib import admin
from .models import *
# Register your models here.

# here we register all the model classes in our admin panel
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
