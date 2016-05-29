from django.contrib.auth.models import User, Group
from .models import Account
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
        fields = ('email',)

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ReferenceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('pk', 'name', 'key_id', 'v_code')

class UpdateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('name', 'key_id', 'v_code')
