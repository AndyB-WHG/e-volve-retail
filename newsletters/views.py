from django.shortcuts import render
from . forms import NewsletterForm, SubscriberForm


def new_newsletter(request):
    form = NewsletterForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletters/new_newsletter.html', context)


def new_subscriber(request):
    form = SubscriberForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletters/subscriber_list.html', context)
