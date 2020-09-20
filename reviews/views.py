from django.shortcuts import render
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def add_review(request):
    """ A view to display all reviews and form for adding new reviews """
    if request.method == 'POST':
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            messages.info(request, 'Your review has been submitted.')
            reviews = Review.objects.all()
            return render(request, 'reviews/reviews.html', {'reviews': reviews})
    else:
        reviews = Review.objects.all()
        context = {
            'reviews': reviews,
        }
    return render(request, 'reviews/reviews.html', context)
