from ..models import RecipeList
from rest_framework import viewsets, permissions, status
from podmon.api.serializers import RecipeListSerializer
from rest_framework.response import Response
from ..permissions import IsOwnerOrReadOnly


class RecipeListView(viewsets.GenericViewSet):
    queryset = RecipeList.objects.all()
    serializer_class = RecipeListSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def retrieve(self, request, pk):
        """ Get a Recipe List """
        user = self.get_object()
        recipe_list_serializer = self.get_serializer(user)
        return Response(recipe_list_serializer.data)

    def destroy(self, request, pk):
        """ Remove a Recipe List """
        user = self.get_object()
        user.remove()
        return Response(200)
