from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    comp_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'comp_count': comp_count,
    }

    return context