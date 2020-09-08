from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def all_reviews(request):
    """ A view to show all site reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/add_review.html', context)


def reviews(request):
    """ A view to display reviews and a form for adding site reviews """
    
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/add_review.html', context)

    if request.method == 'POST':
        add_review = ReviewForm(request.POST)
        if add_review.is_valid():
            add_review.save()
            messages.add_message(request, messages.INFO, 'Your review has been submitted.')
            return redirect(reverse('home'))
    else:
        add_review = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': add_review})