""" Views to display 'All Products' and individual Product Details """

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
# Note: 'Q' Enables searches where the query
# can be in either one list 'or' another
from .models import Product, Category


def all_products(request):
    """ A view to return all the products, including sorting and searching """

    products = Product.objects.all()
    query = None  # Resets the 'query' value in case of a previous search.
    category = None
    full_category_name = None


    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name__icontains=category)
            full_category_name = Category.objects.filter(name__in=category)

            if not products:
                messages.error(request,
                               "Sorry - no products were found")
                return redirect(reverse('products'))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            # Note: 'the 'i' in icontains means 'case insensitive'.
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': full_category_name,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the details of an individual product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
