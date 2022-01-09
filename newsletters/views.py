from django.shortcuts import render


def new_newsletter(request):
    return render(request, 'newsletters/new_newsletter.html')
