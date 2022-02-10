""" Classes to optimise the 'Newsletters' Admin screen """

from django.contrib import admin
from . models import Newsletters, Subscribers


class NewsletterAdmin(admin.ModelAdmin):
    """ Defines layout of 'Newsletters' submenu
    within 'NEWSLETTERS' Admin section """
    list_display = (
        'id',
        'title',
        'body',
        'date',
        'author',
        'id',
    )

    ordering = ('date',)


class SubscriberAdmin(admin.ModelAdmin):
    """ Defines layout of 'Subscribers' submenu
    within 'NEWSLETTERS' Admin section  """
    list_display = (
        'id',
        'email',
        'firstName',
        'lastName',
        'date',
        'id',
    )

    ordering = ('date',)


admin.site.register(Newsletters, NewsletterAdmin)
admin.site.register(Subscribers, SubscriberAdmin)
