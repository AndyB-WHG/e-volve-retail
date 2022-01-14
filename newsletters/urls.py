""" Url patterns for Newsletters and Subscribers """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.new_newsletter, name='new_newsletter'),
    path('subscribe/', views.new_subscriber, name='new_subscriber'),
]
