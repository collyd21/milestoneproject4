from django.shortcuts import render
from .models import Comp

# Create your views here.

def all_comps(request):
    """ A view to show all competitions """

    comps = Comp.objects.all()

    context = {
        'comps': comps,
    }

    return render(request, 'comps/comps.html', context)