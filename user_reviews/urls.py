""" Url's for User Reviews """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_reviews, name='get_all_reviews'),
    path('my_reviews', views.users_reviews, name='users_reviews'),
    path('edit_review/<review_id>', views.edit_review, name='edit_review'),
]
