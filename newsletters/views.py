from django.shortcuts import render


@login_required
def create_newsletter_message(request):
    return render(request, )