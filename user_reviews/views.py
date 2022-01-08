from django.shortcuts import render, redirect, reverse
from . models import User_review
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required


@login_required
def get_all_reviews(request):
    # creates a view to allow Admin Rights users to view all reviews.
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    reviews = User_review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'user_reviews/all_reviews.html', context)


@login_required
def users_reviews(request):
    user = UserProfile.objects.get(user=request.user)
    # creates a view to allow users to see only their own reviews.
    my_reviews = User_review.objects.filter(user=user)
    context = {
        'my_reviews': my_reviews
    }
    return render(request, 'user_reviews/users_reviews.html', context)


@login_required
def edit_review(request, review_id, image_url):
    print("Review id is :", review_id)
    print("Review image url is", image_url)
    user = UserProfile.objects.get(user=request.user)
    review = User_review.objects.get(id=review_id)
    context = {
        'review': review,
        'user': user,
        'image_url': image_url,
    }
    return render(request, 'user_reviews/edit_review.html', context)
