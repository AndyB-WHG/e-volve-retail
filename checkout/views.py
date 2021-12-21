from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

import stripe
from shopping_bag.contexts import shopping_bag_contents 
from .forms import OrderForm


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    shopping_bag_session = request.session.get('shopping_bag_session', {})
    if not shopping_bag_session:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_shopping_bag = shopping_bag_contents(request)
    current_total = current_shopping_bag['total_including_delivery']
    # convert the value into pennies/cents below
    stripe_total = round(current_total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'You need to set your Public Key.  \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
