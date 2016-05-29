
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """ Extended User model """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', related_query_name='account')
    name = models.CharField(max_length=100)
    key_id = models.CharField(max_length=8, unique=True)
    v_code = models.CharField(max_length=65, unique=True)
