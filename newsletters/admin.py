from django.contrib import admin
from . models import CreateNewsletter


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


admin.site.register(CreateNewsletter, NewsletterAdmin)
