""" Views to display 'All Products' and individual Product Details """
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Note: 'Q' Enables searches where the query
# can be in either one list 'or' another
from django.db.models import Q
from django.db.models.functions import Lower
from user_reviews.models import User_review
from profiles.models import UserProfile
from checkout.models import Order

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
    reviews = User_review.objects.all()

    print("Product Detail is for : ", product)
    print("Reviews for this product are: ", reviews)

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def review_product(request, product_id):
    """ A view to allow users to submit reviews """

    product = get_object_or_404(Product, pk=product_id)
    reviews = User_review.objects.all()
    user = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        product_purchased = False
        users_orders = Order.objects.filter(user_profile=user)
        print("users_orders = : ", users_orders)
        print("product = :", product)
        if users_orders:
            for order in users_orders:
                line_items = order.lineitems.all()

                for item in line_items:
                    print("order number : ", order)
                    print("item.product in line_items = :", item.product)
                    if item.product == product:
                        product_purchased = True
                        if request.user.is_authenticated:
                            date = models.DateTimeField(auto_now_add=True)
                            user_review = request.POST.get('review-text')
                            User_review.objects.create(product=product,
                                                       date=date, user=user,
                                                       review_text=user_review)
                            messages.success(request,
                                             'Thank you for your review!')
                            return redirect(reverse('product_detail',
                                            args=[product_id]))

                        return render(request, 'home/index.html')

            if product_purchased is False:
                messages.error(request, 'Sorry, you cannot review\
                        a product unless you have purchased it first.')
                return redirect(reverse('product_detail',
                                args=[product_id]))

        else:
            if product_purchased is False:
                messages.error(request, 'Sorry, you cannot review a\
                        product unless you have purchased it first.')
                return redirect(reverse('product_detail', args=[product_id]))
    else:
        context = {
                'product': product,
                'reviews': reviews,
            }
        return render(request, 'products/product_review.html', context)


@login_required()
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the\
                 form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure\
                 the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required()
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))


    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
