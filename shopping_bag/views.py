from django.shortcuts import render, redirect, reverse


def shopping_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add a quantity of a given item to the Shopping Bag """

    size = None
    if 'size' in request.POST:
        size = request.POST.get('size')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopping_bag_session = request.session.get('shopping_bag_session', {})
    # Note: above gets the session called shopping_bag, but if such
    # a session doesn't exist, it creates an empty dictionary instead.

    if size:
        if item_id in list(shopping_bag_session.keys()):
            if size in shopping_bag_session[item_id]['items_by_size'].keys():
                shopping_bag_session[item_id]['items_by_size'][size] += quantity
            else:
                shopping_bag_session[item_id]['items_by_size'][size] = quantity
        else:
            shopping_bag_session[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(shopping_bag_session.keys()):
            shopping_bag_session[item_id] += quantity
        else:
            shopping_bag_session[item_id] = quantity
        # Checks if the session already includes the item.
        # If it does, it add the quantity to the existing quanity.
        # If it doesn't it add the item_id and it's related quantity.

    request.session['shopping_bag_session'] = shopping_bag_session
    # Over-writes the original shopping bag session with the updated version.

    return redirect(redirect_url)


def edit_shopping_bag(request, item_id):
    """ Allows user to change the item quantity from within the shopping bag """

    size = None
    if 'size' in request.POST:
        size = request.POST.get('size')
    quantity = int(request.POST.get('quantity'))

    shopping_bag_session = request.session.get('shopping_bag_session', {})
    # Note: above gets the session called shopping_bag, but if such
    # a session doesn't exist, it creates an empty dictionary instead.

    if size:
        if quantity > 0:
            shopping_bag_session[item_id]['items_by_size'][size] = quantity
        else:
            del shopping_bag_session[item_id]['items_by_size'][size]

    else:
        if quantity > 0:
            shopping_bag_session['item_id'] = quantity
        else:
            shopping_bag_session.pop['item_id']

    request.session['shopping_bag_session'] = shopping_bag_session
    # Over-writes the original shopping bag session with the updated version.

    return redirect(reverse('shopping_bag'))
