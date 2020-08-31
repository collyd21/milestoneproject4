from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You haven't added to your shoebox yet!")
        return redirect(reverse('comps'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HFNVtDLLXrB81ioVBoQzP8t0ZqMh7vWFRyGJqJOxjN0HZRjClXuLxlHE2A1JeemLzQMpLyfwOwX941OzKGlYOai00ZtquhByY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)