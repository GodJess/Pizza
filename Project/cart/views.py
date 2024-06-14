from django.shortcuts import render, redirect
from django.conf import settings
from .forms import OrderForm
# Create your views here.

def cart(request):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    ak = request.session.get(settings.USER_SESSION_ID,{})
    length = len(cart)
    form = OrderForm(request=request)
    if request.method == "POST":
        forms = OrderForm(request.POST)
        if forms.is_valid():
            forms.save()
            request.session.pop(settings.CART_SESSION_ID, None)
            return redirect('account')        
        
    context = {
        'cart': cart ,
        'length': length,
        'ak': ak,
        'form': form,
               }
    
    return render(request, 'cart/cart.html', context)

def remove_from_cart(request, product_id):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    if str(product_id) in cart: 
        del cart[str(product_id)]
        request.session[settings.CART_SESSION_ID] = cart
    return redirect('cart')
    #if product_id in cart:
        #del cart[product_id]
        #request.session[settings.CART_SESSION_ID] = cart
    #return redirect('cart')

def clear_cart(request):
    request.session.pop(settings.CART_SESSION_ID, None)
    return redirect('cart')

