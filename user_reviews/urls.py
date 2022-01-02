""" Url's for User Reviews """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_reviews, name='get_all_reviews'),
]
