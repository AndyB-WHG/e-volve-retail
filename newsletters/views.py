from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from . models import Subscribers
from . forms import NewsletterForm, SubscriberForm


@login_required
def new_newsletter(request):
    if request.user.is_superuser:
        if request.method == 'POST':

            author = request.user
            print("Author (POST) is : ", author)
            date = models.DateTimeField(auto_now_add=True)
            form_data = {
                'title': request.POST['title'],
                'body': request.POST['body'],
                'date': date,
                'author': author,
            }
            form = NewsletterForm(form_data)
            print("Newsletter form (POST) is : ", form)
            if form.is_valid():
                profile = get_object_or_404(UserProfile, user=request.user)
                newsletter_form = form.save(commit=False)
                newsletter_form.author = profile
                title = form.cleaned_data.get('title')
                body = form.cleaned_data.get('body')
                print("Title = ", title)
                print("Body = ", body)
                form.save()
                subscribers = Subscribers.objects.all()
                subscriber_emails = []
                for subscriber in subscribers:
                    subscriber_emails.append(subscriber.email)
                print("Subscriber email list is : ", subscriber_emails)
                send_mail(
                    title,
                    body,
                    'admin@e-volve-retail.com',
                    subscriber_emails,
                    fail_silently=False,
                )
                messages.success(request, "The newsletter was sent successfully!")
                return redirect('/newsletters/')
        else:
            form = NewsletterForm()
            context = {
                'form': form,
            }
            return render(request, 'newsletters/new_newsletter.html', context)
    else:
        messages.error(request, 'Only website Administrators can do that!')


@login_required()
def new_subscriber(request):
    if request.method == "POST":
        form_data = {
            'firstName': request.POST['firstName'],
            'lastName': request.POST['lastName'],
            'email': request.POST['email'],
        }
        form = SubscriberForm(form_data)
        print("Form = ", form)

        if form.is_valid():
            email = request.POST['email']
            already_subscribed = Subscribers.objects.filter(email=email)
            print("Email is : ", email)
            print("Already Subscribed? : ", already_subscribed)
            if not already_subscribed:
                form.save()

                print("Email = ", email)
                send_mail(
                    'E-volve Retail Newsletter Subscription',
                    'Thank you for subscribing to our Newsletter.',
                    'admin@e-volve-retail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, "Subscription was successful!")
                return redirect('/products')
            else:
                messages.error(request, "You already subscribed with \
                    that email address.")
                return redirect('new_subscriber')
    else:
        form = SubscriberForm()
        context = {
            'form': form,
        }
        return render(request, 'newsletters/subscribe_to_newsletter.html',
                      context)
