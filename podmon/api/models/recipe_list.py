from django.db import models
from django.contrib.auth.models import User


class RecipeList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


class RecipeListMember(models.Model):
    recipe_list = models.ForeignKey(RecipeList, on_delete=models.CASCADE, related_name='members')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
