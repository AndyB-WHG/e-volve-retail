""" Url's for 'Shoppng Bag' pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name="shopping_bag"),
    path('add_item/<item_id>/', views.add_to_shopping_bag,
         name="add_to_shopping_bag"),
    path('adjust_shopping_bag/<item_id>/', views.adjust_shopping_bag,
         name="adjust_shopping_bag"),
    path('delete_from_shopping_bag/<item_id>/', views.delete_from_shopping_bag,
         name="delete_from_shopping_bag"),
]
