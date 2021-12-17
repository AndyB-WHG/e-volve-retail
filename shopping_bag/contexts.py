""" Context Processor for the Shopping Bag variables -
makes the variable available project wide as is listed
in the 'settings.py' context processor section"""

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shopping_bag_contents(request):
    """ Returns a dictionary of the shopping bag items """

    shopping_bag_items = []
    total_order_value = 0
    shopping_bag_count = 0
    delivery_cost = 0
    shopping_bag_session = request.session.get('shopping_bag_session', {})

    for item_id, quantity in shopping_bag_session.items():
        product = get_object_or_404(Product, pk=item_id)
        total_order_value += quantity * product.price
        print(total_order_value)
        shopping_bag_count += quantity
        shopping_bag_items.append ({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total_order_value < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total_order_value * Decimal(
                   settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - (
                              total_order_value)

    else:
        delivery_cost = 0
        free_delivery_delta = 0

    total_including_delivery = total_order_value + delivery_cost

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total_order_value': total_order_value,
        'shopping_bag_count': shopping_bag_count,
        'delivery_cost': delivery_cost,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'total_including_delivery': total_including_delivery,
    }

    return context
