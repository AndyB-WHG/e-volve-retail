""" Views to display 'All Products' and individual Product Details """

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
# Note: 'Q' Enables searches where the query
# can be in either one list 'or' another
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to return all the products, including sorting and searching """

    products = Product.objects.all()
    query = None  # Resets the 'query' value in case of a previous search.
    category = None
    full_category_name = None
    sort = None
    sort_direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'sort_direction' in request.GET:
                sort_direction = request.GET['sort_direction']
                if sort_direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{sort_direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': full_category_name,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the details of an individual product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)