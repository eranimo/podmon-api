
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Extended User model """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_verified = models.BooleanField(default=False)
    verify_email_token = models.CharField(max_length=100, null=True, blank=True)
