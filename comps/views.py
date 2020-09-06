from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Comp
from .forms import CompForm


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


def add_comp(request):
    """ Add a competition to the site """
    if request.method == 'POST':
        form = CompForm(request.POST, request.FILES)
        if form.is_valid():
            comp = form.save()
            messages.success(request, 'Successfully added new competition!')
            return redirect(reverse('comp_info', args=[comp.id]))
        else:
            messages.error(request, 'Failed to add competition. Please ensure the form is valid.')
    else:
        form = CompForm()

    template = 'comps/add_comp.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_comp(request, comp_id):
    """ Edit a competition """
    comp = get_object_or_404(Comp, pk=comp_id)
    if request.method == 'POST':
        form = CompForm(request.POST, request.FILES, instance=comp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated competition!')
            return redirect(reverse('comp_info', args=[comp.id]))
        else:
            messages.error(request, 'Failed to update competition. Please ensure the form is valid.')
    else:
        form = CompForm(instance=comp)
        messages.info(request, f'You are editing {comp.name}')

    template = 'comps/edit_comp.html'
    context = {
        'form': form,
        'comp': comp,
    }

    return render(request, template, context)

def delete_comp(request, comp_id):
    """ Delete a product from the store """
    comp = get_object_or_404(Comp, pk=comp_id)
    comp.delete()
    messages.success(request, 'Competition successfully deleted!')
    return redirect(reverse('comps'))
