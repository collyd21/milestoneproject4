from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ A view to render contact form """
    if request.method == 'POST':
        contact_us = ContactForm(request.POST)
        if contact_us.is_valid():
            contact_us.save()
            messages.add_message(request, messages.INFO, 'Information Submitted.')
            return redirect(reverse('home'))
    else:
        contact_us = ContactForm()
    return render(request, 'contact/contact.html', {'form': contact_us})
