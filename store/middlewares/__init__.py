from .auth import auth_middleware

# middleware folder act as an authentication file between 2 pages. Here middleware is used between home, cart, order and bill page. If user clicked on cart button without logging in than he/she will be redirected to login page. Once the user logs in, then he can view his/her cart, order and bill.