from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware


class Pdf(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        template_path = 'pdf.html'
        context = {'customer': customer,
                   'orders': orders}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        # if we want to download then our reponse variable will look like this inside the bracket (response['Content-Disposition'] = 'attachment; filename="invoice.pdf"') else if we want to pdf to only open in browser than our response variable will look like below
        response['Content-Disposition'] = 'filename="invoice.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
