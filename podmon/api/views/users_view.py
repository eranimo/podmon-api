from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from podmon.api.serializers import (
    DetailedUserSerializer,
    UpdateUserSerializer,
    RecipeListSerializer,
    RecipeSerializer
)
from ..models import RecipeList, Recipe


class UsersView(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = DetailedUserSerializer


    def retrieve(self, request, pk):
        """ Get a User's information """
        user = self.get_object()
        user_serializer = self.get_serializer(user)
        return Response(user_serializer.data)


    def update(self, request, pk):
        """ Get a User's information """
        serializer = UpdateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_object()
            user.username = serializer.data.get('username')
            user.save()
            user_serializer = self.get_serializer(user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """ List all Users """
        users = User.objects.all()

        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @detail_route()
    def recipe_lists(self, request, pk=None):
        """ Returns a User's saved Recipe lists """
        owner = self.get_object()
        recipe_lists = RecipeList.objects.filter(owner=owner)

        context = {
            'request': request
        }

        recipe_list_serializer = RecipeListSerializer(recipe_lists, many=True, context=context)
        return Response(recipe_list_serializer.data)

    @detail_route()
    def owned_recipes(self, request, pk=None):
        """ Returns a User's Posted Recipes """
        owner = self.get_object()
        recipe_lists = Recipe.objects.filter(poster=owner)

        context = {
            'request': request
        }

        recipe_serializer = RecipeSerializer(recipe_lists, many=True, context=context)
        return Response(recipe_serializer.data)
