""" Generate 'Create Newsletter' form within 'new_newsletter page """

from django import forms
from .models import Newsletters, Subscribers


class NewsletterForm(forms.ModelForm):
    """ Create Newsletter Form """
    class Meta:
        """ Choose fields req'd - fields taken from 'Newsletters' model """
        model = Newsletters
        fields = ('title', 'body',)

    # def __init__(self):
    #     self.fields['title'].widget.attrs['autofocus'] = True


class SubscriberForm(forms.ModelForm):
    """ Create form for users to Subscribe to the Newsletters """
    class Meta:
        """ Choose fields req'd - fields taken from 'Subscribers' model """
        model = Subscribers
        fields = ('firstName', 'email',)

    # def __init__(self, *args, **kwargs):
    #     self.fields['firstName'].widget.attrs['autofocus'] = True