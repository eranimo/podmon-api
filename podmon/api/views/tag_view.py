from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from podmon.api.serializers import TagDetailsSerializer
from ..models import Tag


class TagView(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagDetailsSerializer


    def retrieve(self, request, pk):
        """ Get a Tag """
        user = self.get_object()
        user_serializer = self.get_serializer(user)
        return Response(user_serializer.data)

    def list(self, request):
        """ List all Tags """
        tags = Tag.objects.all()

        page = self.paginate_queryset(tags)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(tags, many=True)
        return Response(serializer.data)

    # @detail_route()
    # def recipes(self, request, pk=None):
    #     """ Returns all Recipes with this Tag """
    #     owner = self.get_object()
    #     recipe_lists = Recipe.objects.filter(tag=owner)
    #
    #     context = {
    #         'request': request
    #     }
    #
    #     recipe_list_serializer = RecipeListSerializer(recipe_lists, many=True, context=context)
    #     return Response(recipe_list_serializer.data)
