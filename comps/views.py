from django.shortcuts import render, get_object_or_404
from .models import Comp

# Create your views here.


def all_comps(request):
    """ A view to show all competitions """

    comps = Comp.objects.all()

    context = {
        'comps': comps,
    }

    return render(request, 'comps/comps.html', context)


def comp_info(request, comp_id):
    """ A view to show more information about a particular competition """

    comp = get_object_or_404(Comp, pk=comp_id)

    context = {
        'comp': comp,
    }

    return render(request, 'comps/comp_info.html', context)
