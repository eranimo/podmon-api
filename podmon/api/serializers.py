from django.contrib.auth.models import User, Group
from .models import Recipe, RecipeList, RecipeListMember, Tag
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class ReferenceUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

class DetailedUserSerializer(ReferenceUserSerializer):
    class Meta(ReferenceUserSerializer.Meta):
        fields = ('id', 'username', 'email', 'groups')

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class TagDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'description')



class RecipeSerializer(serializers.ModelSerializer):
    poster = ReferenceUserSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'poster', 'description', 'tags', 'instructions',)


class RecipeListMemberSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(many=False)
    class Meta:
        model = RecipeListMember
        fields = ('id', 'date_added', 'note', 'recipe')

class RecipeListSerializer(serializers.ModelSerializer):
    members = RecipeListMemberSerializer(many=True)
    class Meta:
        model = RecipeList
        fields = ('id', 'title', 'description', 'description', 'members')

    def create(self, validated_data):
        members_data = validated_data.pop('members')
        recipe_list = RecipeList.create(**validated_data)
        for member_data in members_data:
            RecipeListMember.create(recipe_list=recipe_list, **member_data)
        return recipe_list
