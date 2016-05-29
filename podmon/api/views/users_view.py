from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from podmon.api.serializers import (
    DetailedUserSerializer,
    UpdateUserSerializer,
    ReferenceAccountSerializer
)
from ..models import Account


class UsersView(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = DetailedUserSerializer


    def retrieve(self, request, pk):
        """
        Get a User's information
        ---
        serializer: DetailedUserSerializer
        """
        user = self.get_object()
        user_serializer = self.get_serializer(user)
        return Response(user_serializer.data)


    def update(self, request, pk):
        """
        Update a User's information
        ---
        request_serializer: UpdateUserSerializer
        response_serializer: DetailedUserSerializer
        """
        serializer = UpdateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_object()
            user.email = serializer.data.get('email')
            user.save()
            user_serializer = self.get_serializer(user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        List all Users
        ---
        serializer: DetailedUserSerializer
        """
        users = User.objects.all()

        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @detail_route()
    def accounts(self, request, pk=None):
        """
        Returns a User's accounts
        ---
        serializer: ReferenceAccountSerializer
        """
        owner = self.get_object()
        accounts = Account.objects.filter(owner=owner)
        print(accounts)
        context = {
            'request': request
        }

        accounts_serializer = ReferenceAccountSerializer(accounts, many=True, context=context)
        return Response(accounts_serializer.data)
