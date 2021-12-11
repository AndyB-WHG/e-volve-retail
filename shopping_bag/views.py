from django.shortcuts import render


def shopping_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'shopping_bag/shopping_bag.html')