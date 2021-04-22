from django.shortcuts import redirect

# In Django, middleware is a lightweight plugin that processes during request and response execution. Middleware is used to perform a function in the application. The functions can be a security, session, csrf protection, authentication etc. Django provides various built-in middleware and also allows us to write our own middleware. See, 'settings.py' file of Django project that contains various middleware, that is used to provides functionalities to the application. For example, Security Middleware is used to maintain the security of the application. In this app, we have created our middleware to check if the user has a session or not. If user has a session that means he/she has logged in, no one is logged in.


# auth_middleware check one get_response only. Django initializes middleware with parameter 'get_response' only once (1 request at a time). I takes the request and send back the response after checking the constraints. This method is called using get() function in cart.py, order.py and pdf.py. All the calls are in 'urls.py'
def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # print(request.session.get('customer'))

        returnUrl = request.META['PATH_INFO']
        # Django uses request and response objects to pass state through the system. When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Therefore request.META contains the metadata of the object and 'PATH_INFO' contains 'the path information portion of the path'.
        # for example if we have use a webserver at path in urls.py '/omkar_info' and we want to excess the image file in '/uploads/products' folder and say url='../uploads/products' then when we print url.path() it will give the entire path of the image e.g.'/omkar_info/uploads/products/<image.png>' which is not good if we want to test our app on different servers. But if we use url.path_info() then it will give only give the info of the path e.g '/uploads/products/<image.png>'.
        # This is the reason we used 'PATH_INFO'.

        # print(request.META['PATH_INFO'])

        # Sessions are the mechanism used by Django (and most of the Internet) for keeping track of the "state" between the site and a particular browser. Sessions allow you to store arbitrary data per browser, and have this data available to the site whenever the browser connects.

        # request.session.get returns true if the user is logged in, else it will be redirect to the login page.
        print(request.session.get('customer'))
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware
