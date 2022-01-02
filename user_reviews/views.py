from django.shortcuts import render
from . models import User_review


def get_all_reviews(request):
    # create the 'query object' from which we can interrogate the data
    reviews = User_review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'user_reviews/all_reviews.html', context)
