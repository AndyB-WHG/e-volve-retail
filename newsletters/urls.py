from django.urls import path
from . import views


urlpatterns = [
    path('', views.new_newsletter, name='new_newsletter'),
]