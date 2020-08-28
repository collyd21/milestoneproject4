from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from comps.models import Comp
# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified competition to the cart """

    comp = Comp.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    messages.success(request, f'Added {comp.name} to your cart')
    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Remove an item from the cart """
    comp = Comp.objects.get(pk=item_id)
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    messages.success(request, f'Removed {comp.name} from your cart')
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
