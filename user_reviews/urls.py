""" Url's for User Reviews """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_reviews, name='get_all_reviews'),
    path('my_reviews', views.users_reviews, name='users_reviews'),
    path('edit_review/<int:review_id>', views.edit_review, name='edit_review'),
    path('delete_review_user/<int:review_id>', views.delete_review_user,
         name='delete_review_user'),
    path('delete_review_admin/<int:review_id>', views.delete_review_admin,
         name='delete_review_admin'),
]
