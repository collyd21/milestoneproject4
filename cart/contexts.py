from django.shortcuts import get_object_or_404
from comps.models import Comp


def cart_contents(request):

    cart_items = []
    total = 0
    comp_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        comp = get_object_or_404(Comp, pk=item_id)
        total += quantity * comp.price
        comp_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'comp': comp,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'comp_count': comp_count,
    }

    return context
