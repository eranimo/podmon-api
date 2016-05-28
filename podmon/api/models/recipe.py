from django.db import models
from django.contrib.auth.models import User
from podmon.api.constants import UNITS


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_recipes')
    description = models.TextField()
    tags = models.ManyToManyField('Tag')
    instructions = models.TextField()

class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                              height_field='height',
                              width_field='width')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()


class RecipeSection(models.Model):
    recipe = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_section = models.ForeignKey(RecipeSection, on_delete=models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey('Ingredient')
    is_plural = models.BooleanField(default=False)
    quantity = models.PositiveSmallIntegerField(null=True, blank=True)
    unit = models.CharField(max_length=200, choices=UNITS)
    prep_note = models.CharField(max_length=200, null=True, blank=True)
    prep_action = models.CharField(max_length=200, null=True, blank=True)
