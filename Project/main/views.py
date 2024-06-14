from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Public, Role, Combo, Drink, Dessert, MainProduct
from .forms import ArticlesForm, PublicForm
from django.views.generic import DetailView
from  django.conf import settings



# Create your views here.
def index(request):
    object = MainProduct.objects.filter(category="pizza")
    return render(request, 'main/index.html', { 'object' : object})

def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))

    product = MainProduct.objects.get(id=product_id)
    itog = int(product.price) * quantity
    cart = request.session.get(settings.CART_SESSION_ID, {})
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
        cart[product_id]['itog'] +=  (int(product.price) * quantity)
        #cart[product_id] = {'name': product.name, 'price': product.price, 'quantity': quantity, 'image': product.image, "id": product.id, "itog": itog}
    else:
        cart[product_id] = {'name': product.name, 'price': product.price, 'quantity': quantity, 'image': product.image, "id": product.id, "itog": itog}

    
    request.session[settings.CART_SESSION_ID] = cart
    
    return redirect('home')

class NewDatailViewProduct(DetailView):
    model = MainProduct
    template_name = 'main/details_product.html'
    context_object_name = 'article'

def about(request):
    object = Public.objects.all()
    error = ''
    if request.method == "POST":
        forms = PublicForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('about')
        else:
            error = "Форма была не верной"
    form = PublicForm()

    main={
        'form': form,
        'errors': error,
        'object': object
    }
    return render(request, 'main/about.html', main)

def paneladmin(request):
    errors = ''
    if request.method == "POST":
        forms = ArticlesForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        else:
            errors = "Форма была не верной"
    form = ArticlesForm()

    data={
        'form': form,
        'errors': errors
    }

    return render(request, "main/paneladmin.html", data)


def all(request):

    object = MainProduct.objects.all()

    data = {
        "object": object
    }

    return render(request, 'main/all.html', data)


def combo(request):
    object = MainProduct.objects.filter(category="combo")
    return render(request, 'main/combo.html', { 'object' : object})

def dessert(request):
    object = MainProduct.objects.filter(category="dessert")
    return render(request, 'main/dessert.html', { 'object' : object})

def drink(request):
    object = MainProduct.objects.filter(category="drink")
    return render(request, 'main/drink.html', { 'object' : object})

def role(request):
    object = MainProduct.objects.filter(category="role")
    return render(request, 'main/role.html', { 'object' : object})
