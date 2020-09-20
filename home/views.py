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


def how_it_works(request):
    """ A view to return the how it works page """

    return render(request, 'home/how_it_works.html')
