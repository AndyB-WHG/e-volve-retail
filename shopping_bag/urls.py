from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name="shopping_bag"),
    path('add_item/<item_id>/', views.add_to_shopping_bag,
         name="add_to_shopping_bag"),
    path('edit_item/<item_id>/', views.edit_shopping_bag,
         name="edit_shopping_bag"),
]
