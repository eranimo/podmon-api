from django.contrib import admin
from .models import Comment, PantryLocation, PantryItem, RecipeList, RecipeListMember, Recipe, \
                    RecipeImage, RecipeSection, RecipeIngredient, Ingredient, Tag


admin.site.register(Comment)

class PantryLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'date_created', 'is_public')

admin.site.register(PantryLocation, PantryLocationAdmin)

class PantryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredient')

admin.site.register(PantryItem, PantryItemAdmin)
admin.site.register(RecipeList)
admin.site.register(RecipeListMember)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeImage)
admin.site.register(RecipeSection)
admin.site.register(RecipeIngredient)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
