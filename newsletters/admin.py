from django.contrib import admin
from . models import CreateNewsletter, Subscribers


class NewsletterAdmin(admin.ModelAdmin):
    """ Defines layout of 'Newsletters' submenu within 'NEWSLETTERS' Admin section """
    list_display = (
        'title',
        'body',
        'date',
        'author',
        'id',
    )

    ordering = ('date',)


class SubscriberAdmin(admin.ModelAdmin):
    """ Defines layout of 'Subscribers' submenu within 'NEWSLETTERS' Admin section  """
    list_display = (
        'email',
        'firstName',
        'lastName',
        'date',
        'id',
    )

    ordering = ('date',)

admin.site.register(CreateNewsletter, NewsletterAdmin)
admin.site.register(Subscribers, SubscriberAdmin)
