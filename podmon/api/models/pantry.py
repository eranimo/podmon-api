from django.db import models
from django.contrib.auth.models import User


class PantryLocation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField()


class PantryItem(models.Model):
    name = models.CharField('Item Name (custom)', max_length=200, null=True, blank=True)
    ingredient = models.ForeignKey('Ingredient', null=True, verbose_name='Item Name (existing)')
    location = models.ForeignKey(PantryLocation, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
