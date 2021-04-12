// cart functionality

// updateBtns to get all the products with class name "update-cart"
var updateBtns = document.getElementsByClassName("update-cart")

// for loop to iterate through the list of prodcuts
for (var i = 0; i < updateBtns.length; i++) {

    // when 'add to cart' button of paticular product is clicked we need following functionality to occur.
    // addEventListner is the function which  attaches an event handler to the document i.e. html page and we can use multiple types of event handler eg: 'mouseover', 'mouseout', 'click', 'mousemove', etc.
    updateBtns[i].addEventListener('click', function () {

        // in productId we get the id of a paticular product after click
        var productId = this.dataset.product

        // and what action is to be performed is added in action variable
        var action = this.dataset.action

        // console.log('product: ', productId, ' Action: ', action);

        // variable user is defined in head section of main.html to check if the user is logged in or not
        // console.log('USER: ', user);

        // 'AnonymousUser' is inbuilt django variable which checks if the user is authenticated or not
        if (user === 'AnonymousUser') {
            addCookieItem(productId, action)
        }
        else {
            // console.log('User is logged in...');
            // if user is authenticated then following function is called
            updateUserOrder(productId, action)
        }
    })
}

// function to update cart values once the user is authenticated
function updateUserOrder(productId, action) {

    // url variable is used to send the data to a page.
    var url = '/update_item'

    // fetch is used to send data, 1st parameter 'url' is to tell where the data is to be send, 2nd parameter is the object of how and which data to be send - How - Method = POST, Which type of data - 'content-type':'application/json', 3rd parameter is body which a request body, one of "a string(JSON encoded)", "FormData object, to submit the data as form", "Blob/BufferSource to send binary data,"
    fetch(url, {
        method: 'POST', // we will be sending a post data
        headers: {
            // the content type header value is usually auto-set depending on the request body for example we can also do 'content-type':'text/plain;charset=UTF-8' but here we are dealing with json data so we are using the following content-type below. When we are dealing with the post data django always require an authentication that is csrf token.
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action }) // The JSON.stringify() method converts a JavaScript object or value to a JSON string.
        // JSON string is JavaScript Object Notation (JSON) which is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications
    }).then((response) => {
        // .then method is called after the fetch is over
        // here we are returning the reponse which we got in json format
        return response.json();
    }).then((data) => {
        location.reload()
    });
}

function addCookieItem(productId, action) {
    console.log('User is not authenticated')

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 }

        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0) {
            console.log('Item should be deleted')
            delete cart[productId];
        }
    }
    console.log('CART:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    location.reload()
}