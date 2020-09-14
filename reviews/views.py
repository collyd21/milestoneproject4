from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


def all_reviews(request):
    """ A view to display all reviews """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)

@login_required
def add_review(request):
    """ A view to display all reviews and form for adding new reviews """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    if request.method == 'POST':
        add_review = ReviewForm(request.POST)
        if add_review.is_valid():
            add_review.save()
            messages.add_message(request, messages.INFO, 'Your review has been submitted.')
            reviews = Review.objects.all()
            context = {
                'reviews': reviews,
                }
            return render(request, 'reviews/reviews.html', context)
    else:
        add_review = ReviewForm()
    return render(request, 'reviews/reviews.html', context)