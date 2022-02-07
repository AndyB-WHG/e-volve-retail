from django.contrib import admin
from .models import UserProfile

# Register your models here.


class Profiles(admin.ModelAdmin):
    """ Generates 'Products' submenu within 'PRODUCTS' Admin section """
    list_display = (
        'pk',
        'id',
        'user',
        'default_phone_number',
    )


admin.site.register(UserProfile, Profiles)