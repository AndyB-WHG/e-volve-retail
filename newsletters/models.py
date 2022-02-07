""" Models to create newsletters and subscriber list """
from django.db import models
from profiles.models import UserProfile


class Newsletters(models.Model):
    """ Model to create Newsletters """
    class Meta:
        """ Changes the 'Admin section name from
        Newsletterss to Newsletters """
        verbose_name_plural = 'Newsletters'

    title = models.CharField(max_length=75, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, null=True, blank=True,
                               on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Subscribers(models.Model):
    """ Model to add subscribers to the Newsletter list """
    class Meta:
        """ Changes the 'Admin section name from Subscriberss
        to Subscribers """
        verbose_name_plural = 'Subscribers'

    firstName = models.CharField(max_length=25, null=True, blank=True)
    lastName = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
