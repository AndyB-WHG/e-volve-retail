from django.contrib import admin
from .models import User_review


class ReviewAdmin(admin.ModelAdmin):
    """ Defines layout of 'Reviews' submenu within 'REVIEWS' Admin section """
    list_display = (
        'id',
        'user',
        'product',
        'date',
        'review_text',
    )

    ordering = ('user',)

admin.site.register(User_review, ReviewAdmin)
