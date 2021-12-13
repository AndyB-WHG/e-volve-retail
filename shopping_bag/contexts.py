""" Context Processor for the Shopping Bag variables -
makes the variable available project wide as is listed
in the 'settings.py' context processor section"""

def shopping_bag_contents(request):
    """ Returns a dictionary of the shopping bag items """

    shopping_bag_items []
    total = 0
    shopping_bag_count = 0

    context = {}

    return context
