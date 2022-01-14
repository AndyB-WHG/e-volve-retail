"""  Model for creating Product Reviews """

from django.db import models
from products.models import Product
from profiles.models import UserProfile


class User_review(models.Model):
    """ Model to define Review Fields """
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.SET_NULL)
    # Note: 'Set Null' pevents review from being deleted if Product
    # is removed from database
    user = models.ForeignKey(UserProfile, null=True, blank=True,
                             on_delete=models.SET_NULL)
    # Note: 'Set Null' pevents review from being deleted if UserProfile
    # is removed from database
    date = models.DateTimeField(auto_now_add=True)
    review_text = models.CharField(max_length=1028, null=False,
                                   blank=False)

    def __str__(self):
        print("PK = : ", self.id)
        admin_id_1 = self.id
        admin_id_2 = self.user
        full_admin_id = str(admin_id_1) + ". " + str(admin_id_2)
        print("Full admin id = : ", full_admin_id)
        return str(full_admin_id)
