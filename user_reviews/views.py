from django.shortcuts import render, redirect, reverse
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from . models import User_review


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
def edit_review(request, review_id):
    print("Review id is :", review_id)
    user = UserProfile.objects.get(user=request.user)
    review = User_review.objects.get(id=review_id)
    if request.method == 'POST':
        review_text = request.POST.get('review-text')
        print("review_text = ", review_text)
        if user == review.user or request.user.is_superuser:
            if request.user.is_authenticated:
                review.review_text = review_text
                review.save(update_fields=['review_text'])
                messages.success(request, 'The review was successfully\
                     updated.')
        else:
            messages.error(request, "Sorry - only superusers can amend other\
                 users reviews.")
    context = {
        'review': review,
        'user': user,
    }
    return render(request, 'user_reviews/edit_review.html', context)


@login_required
def delete_review_user(request, review_id):
    print("Review id to delete is :", review_id)
    user = UserProfile.objects.get(user=request.user)
    review = User_review.objects.get(id=review_id)
    if user == review.user or request.user.is_superuser:
        if request.user.is_authenticated:
            review.delete()
            return redirect('users_reviews')
    else:
        messages.error(request, "Sorry - only superusers can amend other users\
             reviews.")
        return redirect('users_reviews')


@login_required
def delete_review_admin(request, review_id):
    print("Review id to delete is :", review_id)
    user = UserProfile.objects.get(user=request.user)
    review = User_review.objects.get(id=review_id)
    if request.user.is_superuser:
        if request.user.is_authenticated:
            review.delete()
            return redirect('get_all_reviews')
    else:
        messages.error(request, "Sorry - only superusers can amend other users\
             reviews.")
        return redirect('users_reviews')
