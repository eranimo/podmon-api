from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from podmon.api.serializers import (
    DetailedUserSerializer,
    RegisterUserSerializer
)
from django.db import IntegrityError
from rest_framework_jwt.settings import api_settings
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from smtplib import SMTPException

class UserView(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    @list_route()
    def me(self, request):
        """ Get my information """
        user = request.user
        user_serializer = DetailedUserSerializer(user)
        return Response(user_serializer.data)

    @list_route()
    def verify(self, request):
        user = request.user

        try:
            message = """
            Thank you creating an account on PantryIndex.com. To verify your email address, open the following link:
            http://www.pantryindex.com/verify
            """
            html_message = """
            Thank you creating an account on PantryIndex.com. To verify your email address,
            <a href="http://www.pantryindex.com/verify">Click here</a>
            """
            send_mail('PantryIndex Email Verification',
                      message.strip(),
                      'noreply@pantryindex.com',
                      [user.email],
                      fail_silently=False,
                      html_message=html_message.strip())
            return Response(status=status.HTTP_200_OK)
        except SMTPException:
            return Response({
                error: 'Email failed to send'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
