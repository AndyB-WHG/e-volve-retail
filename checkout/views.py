from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopping_bag_session = request.session.get('shopping_bag_session', {})
    if not shopping_bag_session:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 	'pk_test_51JtUTKKtufOrfNEtCLAmcHtSt1t5k8fMVmnJayGxaSz4ltwTnTSZT8VmO8k8kZuQBVpnoYpFkbeRpQQ2GNEF5C8S0063lJfqO1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
