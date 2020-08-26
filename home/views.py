from django.shortcuts import render
from comps.models import Comp

# Create your views here.


def index(request):
    """ A view to return the index page """

    comps = Comp.objects.all()

    context = {
        'comps': comps,
    }

    return render(request, 'home/index.html', context)
