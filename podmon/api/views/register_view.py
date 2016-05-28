from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from podmon.api.serializers import RegisterUserSerializer
from django.db import IntegrityError
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['POST'])
def register(request):
    """
    Registers a user and returns a token so they can be logged in.
    ---
    parameters:
        - name: username
          description: New user's username
          required: true
          type: string
        - name: password
          description: New user's password
          required: true
          type: string
        - name: email
          description: New user's email
          required: true
          type: string
    """
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    user = User(username=username, email=email, password=password)
    try:
        user.save()
    except IntegrityError as e:
        return Response({
            'error': 'This username has already been taken.'
        }, status=status.HTTP_400_BAD_REQUEST)

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    user_serializer = RegisterUserSerializer(user)
    if user_serializer.is_valid:
        return Response({
            'token': token,
            'user': user_serializer.data
        })
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
