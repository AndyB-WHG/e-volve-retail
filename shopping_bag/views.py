""" Views to generate and amend the 'Shopping Bag' page  """

from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Product


def shopping_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add a quantity of a given item to the Shopping Bag """

    product = get_object_or_404(Product, pk=item_id)
    size = None
    size = request.POST.get('size')
    print("Size = ", size)
    if 'size' in request.POST:
        size = request.POST.get('size')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopping_bag_session = request.session.get('shopping_bag_session', {})
    # Note: above gets the session called shopping_bag, but if such
    # a session doesn't exist, it creates an empty dictionary instead.

    print("Shopping bag session (from add_to_shopping_bag) : ",
          shopping_bag_session)
    print("item_id (from add_to_shopping_bag) : ", item_id)
    print("Size (from add_to_shopping_bag) : ", size)
    print("Quantity (from add_to_shopping_bag) : ", quantity)
    print("Var type of quantity in shopping bag:")

    if size:
        if item_id in list(shopping_bag_session.keys()):
            if size in shopping_bag_session[item_id]['items_by_size'].keys():
                shopping_bag_session[item_id]['items_by_size'][
                    size] += quantity
                messages.success(request, f'Updated size {size.upper()} \
                    {product.name} quantity to \
                        {shopping_bag_session[item_id]["items_by_size"]}')
            else:
                shopping_bag_session[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} \
                    {product.name} to your bag')
        else:
            shopping_bag_session[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} \
                {product.name} to your bag')
    else:
        if item_id in list(shopping_bag_session.keys()):
            shopping_bag_session[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to \
                {shopping_bag_session[item_id]}')
        else:
            # Check if the session already includes the item.
            # If it does, add the quantity to the existing quanity.
            # If it doesn't, add the item_id and it's related quantity.
            shopping_bag_session[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # Over-write the original shopping bag session with the updated version.
    request.session['shopping_bag_session'] = shopping_bag_session

    return redirect(redirect_url)


def adjust_shopping_bag(request, item_id):
    """ Allows user to change item quantity from within the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    size = None
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    quantity = int(request.POST.get('quantity'))

    # Get the session called shopping_bag, but if such
    # a session doesn't exist, create an empty dictionary instead.
    shopping_bag_session = request.session.get('shopping_bag_session', {})

    if size:
        if quantity > 0:
            shopping_bag_session[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} \
                {product.name} quantity to {quantity}')

            # {shopping_bag_session[item_id]["items_by_size"]}')
        else:
            del shopping_bag_session[item_id]['items_by_size'][size]
            if not shopping_bag_session[item_id]['items_by_size']:
                shopping_bag_session.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} \
                {product.name} from your bag')

    else:
        print("There was no size. Replacing previous qty with new quantity.")
        if quantity > 0:
            shopping_bag_session[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to \
                {shopping_bag_session[item_id]}')
            print("Updated shopping_bag_session : ", shopping_bag_session)
        else:
            shopping_bag_session.pop[item_id]
            messages.success(request, f'Removed {product.name} \
                from your shopping bag')

    request.session['shopping_bag_session'] = shopping_bag_session
    # Over-writes the original session cookie with the updated version.

    return redirect(reverse('shopping_bag'))


def delete_from_shopping_bag(request, item_id):
    """ Remove an item from the shopping bag """

    try:
        print("starting the 'Delete From Shopping Bag' function")
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST.get('product_size')

        shopping_bag_session = request.session.get('shopping_bag_session', {})
        # Note: above gets the session called shopping_bag, but if such
        # a session doesn't exist, it creates an empty dictionary instead.

        print("'Delete item' shopping bag session: ", shopping_bag_session)
        print("Item ID being updated : ", item_id)

        if size:
            # Delete the item with the specific size
            del shopping_bag_session[item_id]['items_by_size'][size]
            # If the item only had 1 size stored which is now deleted,
            # delete the item entirely.
            if not shopping_bag_session[item_id]['items_by_size']:
                shopping_bag_session.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} \
                    {product.name} from your bag')

        else:
            shopping_bag_session.pop(item_id)
            messages.success(request, f'Removed {product.name} from your \
                shopping bag')

        request.session['shopping_bag_session'] = shopping_bag_session
        # Over-writes the original session cookie with the updated version.

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=200)
